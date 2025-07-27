def clean_phone(dirty_phone):
    # ASSUME dirty_phone is in format: "773-724-0301"
    # RESULT clean_result is in format "+17737240301"

    clean_result = dirty_phone.replace("-", "")
    return "+1" + clean_result

def clean_email(dirty_email):


    clean_result = dirty_email
    return clean_result
