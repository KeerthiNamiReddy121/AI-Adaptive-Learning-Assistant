def determine_level(score):
    """
    Determine the user's learning level based on performance.
    """

    if score < 50:
        return "Beginner"
    elif score < 80:
        return "Intermediate"
    else:
        return "Advanced"


def get_adaptive_message(level):
    """
    Return personalized guidance based on the user's
    current learning level.
    """

    if level == "Beginner":
        return (
            "Additional explanations and learning support "
            "are recommended."
        )
    elif level == "Intermediate":
        return (
            "You are making good progress. Continue with "
            "moderate-level learning activities."
        )
    else:
        return (
            "Excellent performance! You are ready for "
            "more challenging learning activities."
        )


def get_adaptive_hint(level):
    """
    Change the amount of assistance based on the
    user's learning level.
    """

    if level == "Beginner":
        return (
            "Detailed Hint: Think carefully about the key "
            "definitions and concepts you have learned."
        )
    elif level == "Intermediate":
        return (
            "Hint: Review the main concept before choosing "
            "your answer."
        )
    else:
        return (
            "Advanced Mode: Hints are reduced because your "
            "performance demonstrates strong understanding."
        )