from celery import shared_task

@shared_task
def send_invitation_email(email, org_name, invite_link):
    print('Simulated email to ' + email + ': Join ' + org_name + ' at ' + invite_link)
    return True
