"""Models for clauset."""

from django.db import models


class Clause(models.Model):
    ALABAMA = "AL"
    ALASKA = "AK"
    ARIZONA = "AZ"
    ARKANSAS = "AR"
    CALIFORNIA = "CA"
    COLORADO = "CO"
    CONNECTICUT = "CT"
    DELAWARE = "DE"
    FLORIDA = "FL"
    GEORGIA = "GA"
    HAWAII = "HI"
    IDAHO = "ID"
    ILLINOIS = "IL"
    INDIANA = "IN"
    IOWA = "IA"
    KANSAS = "KS"
    KENTUCKY = "KY"
    LOUISIANA = "LA"
    MAINE = "ME"
    MARYLAND = "MD"
    MASSACHUSETTS = "MA"
    MICHIGAN = "MI"
    MINNESOTA = "MN"
    MISSISSIPPI = "MS"
    MISSOURI = "MO"
    MONTANA = "MO"
    NEBRASKA = "NE"
    NEVADA = "NV"
    NEW_HAMPSHIRE = "NH"
    NEW_JERSEY = "NJ"
    NEW_MEXICO = "NM"
    NEW_YORK = "NY"
    NORTH_CAROLINA = "NC"
    NORTH_DAKOTA = "ND"
    OHIO = "OH"
    OKLAHOMA = "OK"
    OREGON = "OR"
    PENNSYLVANIA = "PA"
    RHODE_ISLAND = "RI"
    SOUTH_CAROLINA = "SC"
    SOUTH_DAKOTA = "SD"
    TENNESSEE = "TN"
    TEXAS = "TX"
    UTAH = "UT"
    VERMONT = "VT"
    VIRGINIA = "VA"
    WASHINGTON = "WA"
    WEST_VIRGINIA = "WV"
    WISCONSIN = "WI"
    WYOMING = "WY"
    UNKNOWN = "UK"
    GOVERNING_LAW_CHOICES = [
        (ALABAMA, "Alabama"),
        (ALASKA, "Alaska"),
        (ARIZONA, "Arizona"),
        (ARKANSAS, "Arkansas"),
        (CALIFORNIA, "California"),
        (COLORADO, "Colorado"),
        (CONNECTICUT, "Connecticut"),
        (DELAWARE, "Delaware"),
        (FLORIDA, "Florida"),
        (GEORGIA, "Georgia"),
        (HAWAII, "Hawaii"),
        (IDAHO, "Idaho"),
        (ILLINOIS, "Illinois"),
        (INDIANA, "Indiana"),
        (IOWA, "Iowa"),
        (KANSAS, "Kansas"),
        (KENTUCKY, "Kentucky"),
        (LOUISIANA, "Louisana"),
        (MAINE, "Maine"),
        (MARYLAND, "Maryland"),
        (MASSACHUSETTS, "Massachusetts"),
        (MICHIGAN, "Michigan"),
        (MINNESOTA, "Minnesota"),
        (MISSISSIPPI, "Mississippi"),
        (MISSOURI, "Missouri"),
        (MONTANA, "Montana"),
        (NEBRASKA, "Nebraska"),
        (NEVADA, "Nevada"),
        (NEW_HAMPSHIRE, "New Hampshire"),
        (NEW_JERSEY, "New Jersey"),
        (NEW_MEXICO, "New Mexico"),
        (NEW_YORK, "New York"),
        (NORTH_CAROLINA, "North Carolina"),
        (NORTH_DAKOTA, "North Dakota"),
        (OHIO, "Ohio"),
        (OKLAHOMA, "Oklahoma"),
        (OREGON, "Oregon"),
        (PENNSYLVANIA, "Pennsylvania"),
        (RHODE_ISLAND, "Rhode Island"),
        (SOUTH_CAROLINA, "South Carolina"),
        (SOUTH_DAKOTA, "South Dakota"),
        (TENNESSEE, "Tennessee"),
        (TEXAS, "Texas"),
        (UTAH, "Utah"),
        (VERMONT, "Vermont"),
        (VIRGINIA, "Virginia"),
        (WASHINGTON, "Washington"),
        (WEST_VIRGINIA, "West Virginia"),
        (WISCONSIN, "Wisconsin"),
        (WYOMING, "Wyoming")
        (UNKNOWN, "Unknown")
    ]

    topic = models.CharField(max_length=200)
    contract_type = models.CharField(max_length=200)
    # Date clause is approved to be added to the db.
    date_added = models.DateField()
    # Effective date of contract in which clause appears.
    effective_date = models.DateField()
    gov_law = models.CharField(
        max_length=2,
        choices=GOVERNING_LAW_CHOICES,
        default=UNKNOWN,
        )

    def _str_(self):
        return f"{self.clause_type} {self.date_added}"

