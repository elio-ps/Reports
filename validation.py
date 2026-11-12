TITLE_MIN = 1
TITLE_MAX = 80
DESCRIPTION_MIN = 10
DESCRIPTION_MAX = 500


def validate_report(title, description):
    errors = {}

    if not TITLE_MIN <= len(title) <= TITLE_MAX:
        errors["title"] = f"Title must be between {TITLE_MIN} and {TITLE_MAX} characters."

    if not DESCRIPTION_MIN <= len(description) <= DESCRIPTION_MAX:
        errors["description"] = (
            f"Description must be between {DESCRIPTION_MIN} and {DESCRIPTION_MAX} characters."
        )

    return errors
