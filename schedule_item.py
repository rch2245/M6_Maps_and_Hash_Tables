"""Defines the ScheduleItem dataclass used to represent a single course entry."""

from dataclasses import dataclass


@dataclass
class ScheduleItem:
    """A single row of the course schedule."""

    subject: str
    catalog: str
    section: str
    component: str
    session: str
    units: int
    tot_enrl: int
    cap_enrl: int
    instructor: str

    def get_key(self) -> str:
        """Return the unique dictionary key: Subject_Catalog_Section."""
        return f"{self.subject}_{self.catalog}_{self.section}"

    def print(self) -> None:
        """Print this item as a single formatted row matching the report layout."""
        print(
            f"{self.subject:<8} {self.catalog:<8} {self.section:<8} "
            f"{self.component:<10} {self.session:<8} "
            f"{self.units:>5} {self.tot_enrl:>8} {self.cap_enrl:>8}  "
            f"{self.instructor}"
        )
