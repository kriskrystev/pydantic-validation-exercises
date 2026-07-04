from datetime import date

from pydantic import BaseModel, model_validator


class DateRange(BaseModel):
    start_date: date
    end_date: date

    @model_validator(mode="after")
    def validate_end_after_start(self) -> "DateRange":
        if self.end_date < self.start_date:
            raise ValueError("End date must be after start date.")
        return self
