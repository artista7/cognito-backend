def appicationSignalHandler(**kwargs):
    print(kwargs)
    if kwargs.get("created"):
        pass
    elif kwargs.get("update_fields"):
        pass
