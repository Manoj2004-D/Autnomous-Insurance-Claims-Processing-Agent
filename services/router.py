def recommend_route(data, missing_fields):


    if len(missing_fields) > 0:
        return ("Manual Review","Mandatory fields are missing.")


    description = str(
        data.get("description", "")).lower()

    keywords = ["fraud","staged","inconsistent"]

    for word in keywords:
        if word in description:
            return (
                "Investigation Flag",f"Description contains '{word}'.")


    claim_type = str(
        data.get("claimType", "")
    ).lower()

    if claim_type == "injury":
        return (
            "Specialist Queue",
            "Injury claim."
        )

    damage = data.get("estimatedDamage")

    try:

        damage = data.get("estimatedDamage")
        
        if damage is not None:

            if damage < 25000:
                return (
                "Fast-track",
                "Estimated damage is below ₹25,000.")
        
        


    except:
        pass

    return (
        "Standard Processing",
        "No special routing rule matched."
    )