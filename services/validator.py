MANDATORY_FIELDS = [
    "policyNumber",
    "policyholderName",
    "incidentDate",
    "incidentTime",
    "location",
    "description",
    "claimant",
    "contactDetails",
    "assetType",
    "assetId",
    "estimatedDamage",
    "claimType",
    "attachments",
    "initialEstimate"
]


def validate_claim(data):

    missing_fields = []

    for field in MANDATORY_FIELDS:

        value = data.get(field)

        if value is None:
            missing_fields.append(field)

        elif isinstance(value, str) and value.strip() == "":
            missing_fields.append(field)

    return missing_fields