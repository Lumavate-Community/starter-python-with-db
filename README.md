# Email Service

## Routes

### Route: /send

#### Call: POST

*** Communication: server-server only

Purpose: Send an email to a list of recipients.

Headers:<br/>
Authorization: Bearer{{access_token}}<br/>
Content-Type: application/json

Without Attachment:<br/>
Body:<br/>
```bash
{
	"recipients":"{{recipient_email_addresses}}",
	"subject":"{{email_subject}}",
	"htmlContent":"{{email_html_content}}",
	"textContent":"{{email_text_content}}"
}
```

Expected Response:
```bash
{
  "payload": {
    "data": {
      "hasAttachment": false,
      "html_content": "{{email_html_content}}",
      "id": 1,
      "isBaseCredentials": true,
      "messageId": "dev-test",
      "namespace": "abc",
      "sentAt": "Mon, 11 Mar 2019 14:31:36 GMT",
      "sentBy": "ic/magiclink|email|1",
      "sentFrom": "noreply@localhost:5001",
      "sentTo": "{{recipient_email_addresses}}",
      "text_content": "{{email_text_content}}"
    }
  }
}
```


With Attachment:<br/>
Body:
```bash
{
	"recipients":"{{recipient_email_addresses}}",
	"textContent":"{{email_text_content}}",
  "htmlContent":"{{email_html_content}}",
	"subject":"{{email_subject}}",
	"attachment": {
		"filename":"{{attachment_name}}",
		"data":"{{base64_file_data}}"
	}
}
```

Expected Response:
```bash
{
  "payload": {
    "data": {
      "hasAttachment": true,
      "html_content": "{{email_html_content}}",
      "id": 1,
      "isBaseCredentials": true,
      "messageId": "dev-test",
      "namespace": "abc",
      "sentAt": "Mon, 11 Mar 2019 14:31:36 GMT",
      "sentBy": "ic/magiclink|email|1",
      "sentFrom": "noreply@localhost:5001",
      "sentTo": "{{recipient_email_addresses}}",
      "text_content": "{{email_text_content}}"
    }
  }
}
```


### Route: /templates/{{template_id}}/send

#### Call: POST

Purpose: Send an email to a list of recipients using an email template.  The properties of the email template can be set within the microservice's property sheet.

Headers:<br/>
Authorization: Bearer{{access_token}}<br/>
Content-Type: application/json

Body: The recipients email addresses must be set, along with any properties set in the template data.

```bash
{
	"recipients":"{{email_addresses}}",
	"data":{
		"{{templateFieldNames}}":"{{template_field_data}}"
	}
}
```

Expected Response:
```bash
{
  "payload": {
    "data": {
      "hasAttachment": false,
      "html_content": "{{html_content}}",
      "id": 1,
      "isBaseCredentials": true,
      "messageId": "dev-test",
      "namespace": "abc",
      "sentAt": "Mon, 11 Mar 2019 15:13:41 GMT",
      "sentBy": "ic/magiclink|email|1",
      "sentFrom": "noreply@localhost:5001",
      "sentTo": "{{recipient_email_addresses}}",
      "text_content": "{{text_content}}"
    }
  }
}
```


### Route: /history

#### Call: GET

Purpose: View the history of emails sent using this microservice.

Headers:<br/>
Authorization: Bearer{{access_token}}<br/>
Content-Type: application/json

Expected Response:
```bash
{
  "payload": {
    "currentItemCount": 2,
    "data": [
      {
        "hasAttachment": false,
        "html_content": "{{email_html_content}}",
        "id": 1,
        "isBaseCredentials": true,
        "messageId": "dev-test",
        "namespace": "abc",
        "sentAt": "Fri, 08 Mar 2019 20:20:50 GMT",
        "sentBy": "ic/magiclink|email|1",
        "sentFrom": "noreply@localhost:5001",
        "sentTo": "{{recipient_email_addresses}}",
        "text_content": "{{email_text_content}}"
      },
      {
        "hasAttachment": false,
        "html_content": "{{email_html_content}}",
        "id": 2,
        "isBaseCredentials": true,
        "messageId": "dev-test",
        "namespace": "abc",
        "sentAt": "Fri, 08 Mar 2019 20:20:50 GMT",
        "sentBy": "ic/magiclink|email|1",
        "sentFrom": "noreply@localhost:5001",
        "sentTo": "{{recipient_email_addresses}}",
        "text_content": "{{email_text_content}}"
      }
    ]
  }
}
```
