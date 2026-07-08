from pydantic import BaseModel
from typing import Optional


class ClaimData(BaseModel):

    policyNumber: Optional[str] = None
    policyholderName: Optional[str] = None
    effectiveDates: Optional[str] = None

    incidentDate: Optional[str] = None
    incidentTime: Optional[str] = None
    location: Optional[str] = None
    description: Optional[str] = None

    claimant: Optional[str] = None
    thirdParties: Optional[str] = None
    contactDetails: Optional[str] = None

    assetType: Optional[str] = None
    assetId: Optional[str] = None

    estimatedDamage: Optional[int] = None

    claimType: Optional[str] = None
    attachments: Optional[str] = None
    initialEstimate: Optional[int] = None