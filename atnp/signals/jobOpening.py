"""
    Subscriptions: 

    College: 
        On creation of college and user add these 
            college_college_id -> Messages go to college users and admins 
        On Creation of drive:
            student_drive_drive_id -> Messages go to the students in drive
            company_drive_drive_id -> All companies in the drive
            college_drive_id -> All College users having access to drive 
        On Creation of Company In drive: 
            company_companyInDrive_companyInDriveId -> Messages to company users having access to this
            college_companyInDrive_companyInDriveId -> Message to user having access to company in drive 

"""

def jobOpeningSignalHandler(**kwargs):
    if kwargs.get("created"):
        # when created add the company people as subscribers and 
        # Send notification in college_drive channel that a new jobopening has been made 
        pass
    elif kwargs.get("update_fields"):
        # When the status is updated and been moved to verified, then send notifications 
        # to student college channel that a new job opening is available 
        pass
