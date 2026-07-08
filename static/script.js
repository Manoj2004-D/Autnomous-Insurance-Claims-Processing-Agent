async function uploadFile(){

    const file=document.getElementById("file");

    if(file.files.length===0){

        alert("Please select a PDF/TXT file");

        return;
    }

    const formData=new FormData();

    formData.append("file",file.files[0]);

    document.getElementById("loading").classList.add("active");
    const response=await fetch("/process-claim",{

        method:"POST",

        body:formData

    });

    const data=await response.json();

    document.getElementById("loading").classList.remove("active");
    console.log(data);
    displayResult(data);

}

function displayResult(data){

    let color = "#28a745";

    if(data.recommendedRoute === "Manual Review")
        color = "#ff9800";

    if(data.recommendedRoute === "Investigation Flag")
        color = "#dc3545";

    if(data.recommendedRoute === "Specialist Queue")
        color = "#2196f3";

    let html = "";

    // 1. Extracted Fields
    html += `
        <div class="card">
            <h3>Extracted Fields</h3>
            <pre>${JSON.stringify(data.extractedFields, null, 4)}</pre>
        </div>
    `;

    // 2. Missing Fields
    html += `
        <div class="card">
            <h3>Missing Fields</h3>
            <pre>${
                data.missingFields.length
                    ? JSON.stringify(data.missingFields, null, 4)
                    : "None"
            }</pre>
        </div>
    `;

    // 3. Recommended Route
    html += `
        <div class="card">
            <h3>Recommended Route</h3>

            <div
                style="
                    font-size:24px;
                    font-weight:bold;
                    color:${color};
                ">
                ${data.recommendedRoute}
            </div>

        </div>
    `;

    // 4. Reason
    html += `
        <div class="card">
            <h3>Reason</h3>
            <p>${data.reasoning}</p>
        </div>
    `;

    document.getElementById("result").innerHTML = html;
}