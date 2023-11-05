"""Models for clauset."""

import datetime

from django.db import models
from django.utils import timezone


class Clause(models.Model):
    """Contract clauses."""

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
        (WYOMING, "Wyoming"),
        (UNKNOWN, "Unknown"),
    ]

    text = models.CharField(max_length=2000, default="")
    topic = models.CharField(max_length=200)
    contract_type = models.CharField(max_length=200)
    # Date that clause was approved to be added to db
    pub_date = models.DateTimeField()
    # Effective date of contract in which clause appears.
    effective_date = models.DateField()
    gov_law = models.CharField(
        "governing law",
        max_length=2,
        choices=GOVERNING_LAW_CHOICES,
        default=UNKNOWN,
        )

    def __str__(self):
        return f'{self.topic} ({self.pub_date.date()}): "{self.text[:50]}"'

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=7)


class Rating(models.Model):
    """Up/downvotes and reports from users on contract clauses."""

    clause = models.ForeignKey(Clause, on_delete=models.CASCADE)
    user = models.CharField(max_length=200, default="")
    value = models.CharField(
        max_length=1,
        choices=[
            ("U", "upvote"),
            ("D", "downvote"),
            ("R", "report"),
            ("N", "none")
        ],
        default="N"
    )
    report_reason = models.CharField(max_length=2000)


