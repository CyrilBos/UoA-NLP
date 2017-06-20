"""from Database.DatabaseHelper import DatabaseHelper

connect_string = 'dbname=uoa-nlp user=admin'
db = DatabaseHelper(connect_string)


questions_sentences = []

questions_sentences.append({
    'question_id': 45385,
    'sentences': (
        ('First scenario:I am using the PUT method to create an invoice in Xero,',
         'introduction'),
        ('I have an issue with the lineAmount when a CurrencyRate apply.',
         'problem'),
        ('This is one of my LineItems in my Invoice XML:LineItem\tDescription: EDGA01:INVBE3983:Travel\tLineAmount: 66.201300\tTaxAmount: 0.0000\tAccountCode: RET300\tCurrency fields as part of the Invoice XML:CurrencyCode: USDCurrencyRate: 0.0743The lineItem in the response from XERO, looked like this for the above line item:{          "Description": "EDGA01:INVBE3983:Travel",          "UnitAmount": 66.20,          "TaxType": "NONE",          "TaxAmount": 0.00,          "LineAmount": 66.20,          "AccountCode": "RET300",          "Tracking": ,          "Quantity": 1.0000,          "LineItemID": "732ca155-e1bc-4fe0-bb77-504f25540034",          "ValidationErrors": },',
         'code'),
        ('Why does the LineAmount change to 66.20, does XERO only accepts 2 decimal points?',
         'question'),
        ('Second scenario:I decided to send through the lineAmount with 2 decimal points.',
        'introduction'),
        ('This is one of my LineItems in my Invoice XML:LineItem\tDescription: ILLI11:INVBE3985:Setup\tLineAmount: 224.25\tTaxAmount: 0.00\tAccountCode: ASC400Currency fields as part of the Invoice XML:CurrencyCode: EURCurrencyRate: 0.0690',
         'code'),
        ('So according to my understanding Xero should do a reverse calculation for the value in the Revenue account: 224.25 % 0.0690 = R3250.00, but instead the Revenue account reports R3249.99',
         'problem')
    )
})

questions_sentences.append({
    'question_id': 45515,
    'sentences': (
        ('Hi,I am trying to modify a paid invoice by changing the account_code for given line item. I can modified unpaid invoice with out a problem.',
         'introduction'),
        ('However once the payment exist, I receive the error: "Invoice not of valid status for modification"\
Which makes sense, however I was hoping since I am able to change the item account code easily on the web UI, even if an payment has been created,\
    that I could do the same thing via the API.',
         'problem'),
        ('Any ideas are highly appreciated,thank youJacob',
         'outroduction')
    )
})

questions_sentences.append({
    'question_id': 44498,
    'sentences': (
        ('Hi,We are trying to integrate Xero into our web based application for accounting .',
         'introduction'),
        ('We have different versions of same product running on cloud . each client has its own url like https ://<<clientname>>.ourproduct.com.',
         'introduction'),
        ('Will you please suggest what app type we should use ?',
         'question')
    )
})

questions_sentences.append({
    'question_id': 45329,
    'sentences': (
        ('Hi GuysI did a quick search for this but couldn\'t find an answer I was looking for. The documentation describes:  "Daily Limit: 5000 calls in a rolling 24 hour window"',
         'introduction'),
        ('We have different versions of same product running on cloud . each client has its own url like https ://<<clientname>>.ourproduct.com.',
         'introduction'),
        ('At what time does the count reset?',
         'question'),
        ('Is this relative to the API token you are using and when this is created, or is it every 00:00UTC? or at some other time?',
         'question'),
        ('I\'d like to track the API calls we make to ensure we throttle properly so we never hit the limit, however thats difficult to program unless I know when the API limits are reset.',
         'problem'),
        ('Thanks,Chris',
         'outroduction')
    )
})

questions_sentences.append({'question_id': 45018,
    'sentences': (
        ('Hi,I\'m using the .NET wrapper and want to use the Contact settings as default for the lineitem details.',
         'introduction'),
        ('Specifically, I want to apply a discount or determine whether items are tax inclusive or exclusive based off of the account.',
         'problem'),
        ('Can someone point out how to do that?',
         'question'),
        ('Here\'s my code.Dim wInvoice As New XeroApi.Model.Invoice        Dim wContact As New XeroApi.Model.Contact        Dim Contact Name As String        ContactName = "Test Contact"        Dim myContacts = From contacts In repository.Contacts                         Where contacts.Name = ContactName        For Each myContact As XeroApi.Model.Contact In myContacts            Dim myContactID As String = myContact.ContactID.ToString            wContact.ContactID = New System.Guid(myContactID)            wInvoice.Contact = wContact            wInvoice.InvoiceNumber = "TEST"            wInvoice.Date = "10-29-2015"            wInvoice.Type = "ACCREC"            wInvoice.DueDate = "10-30-2015"            wInvoice.Status = "DRAFT"            wInvoice.LineItems = New XeroApi.Model.LineItems            Dim wLineItem = New XeroApi.Model.LineItem            wLineItem.Quantity = 2            wLineItem.Description = "Item1"            wLineItem.ItemCode = 9            wInvoice.LineItems.Add(wLineItem)            wLineItem = New XeroApi.Model.LineItem            wLineItem.Quantity = 3            wLineItem.Description = "Item2"            wLineItem.ItemCode = 1            wInvoice.LineItems.Add(wLineItem)            wLineItem = New XeroApi.Model.LineItem            wLineItem.Quantity = 4            wLineItem.Description = "Item3"            wLineItem.ItemCode = 17            wInvoice.LineItems.Add(wLineItem)            Dim sResults = repository.Create(Of XeroApi.Model.Invoice)(wInvoice)            If sResults.ValidationErrors.Count = 0 Then                MsgBox("Invoice Created")            Else                For Each something In sResults.ValidationErrors                    MsgBox(something.Message)                Next            End If        Next',
         'code'),
        ('Thanks!',
         'outroduction'),

    )
})

questions_sentences.append({
    'question_id': 45181,
    'sentences': (
        ('With a payment that is part of a bulk payment this returns the first purchase invoice associated with the bulk payment rather than the correct purchase invoice',
         'problem'),
        ('based on the payment amount it seems like a bulk payment divides into smaller payments but the invoice does not correspond)',
         'problem'),
        ('foreach (Payment vo_payment in repository.Payments.Where(x => (x.Date > datebegin && x.Date < dateend && !(x.Status == "DELETED" || x.Status == "VOIDED") && x.Invoice.Type == "ACCPAY")))                {                    vs_paymentstring = Convert.ToDateTime(vo_payment.Date).ToString("yyyyMMdd") + "_" + vo_payment.Invoice.InvoiceNumber + "_(" + vo_payment.PaymentID + ")";',
         'code')
    )
})

questions_sentences.append({
    'question_id': 45011,
    'sentences': (
        ('Hi there,Firstly, apologies if this is in the wrong place.',
         'introduction'),
        ('There were at least 3 possible places this question could\'ve been created, but I figured as I\'m using wrapper code it should go here.',
         'introduction'),
        ('I\'m using the .NET Xero API SDK 2.0.20 in C#.I\'m trying to send an invoice to a customer upon payment.',
         'introduction'),
        ('It should be sent with the invoice in a paid state (so there is no confusion).',
         'introduction'),
        ('I\'ve got the code down good to apply the payment to the invoice, and sending the e-mail goes fine.',
         'introduction'),
        ('But then when we try to update the invoice to say it\'s been sent out, I get the following validation errors:* "Invoice not of valid status for modification"* "This document cannot be edited as it has a payment or credit note allocated to it."',
         'problem'),
        ('Here is some of the code I\'m using. {\t// bits and bobs to get the payment made\t_privateAppApi.Payments.Create(payment);\tEmailInvoice(payment);\tUpdateXeroInvoiceSentToContact(payment.Invoice);}private void UpdateXeroInvoiceSentToContact(XeroModels.Invoice invoice){\tinvoice.SentToContact = true;\t_privateAppApi.Invoices.Update(invoice);}',
         'code'),
        ('Any ideas of how this could/should be handled?',
         'question'),
        ('I thought about trying to set the sent status first, then applying the payment and then sending the e-mail. The problem with this approach is that I\'d get caught out again if something went wrong sending the e-mail, I wouldn\'t then be able to set SentToContact to false, because a payment has been applied. Which doesn\'t feel quite right.',
         'problem'),
        ('Any help appreciated.Cheers,Craig',
         'outroduction')
    )
})

questions_sentences.append({
    'question_id': 45868,
    'sentences': (
        ('I am trying to work out the best way to update an existing Timesheet (Australian Payroll API), without replacing or overwriting the existing TimesheetLines.',
         'introduction'),
        ('At the moment when POSTING and specifying the TimesheetID, the existing TimesheetLines are lost.',
         'problem'),
        ('Also if the Timesheet is Approved then you can no longer POST to it.',
         'problem'),
        ('Having to rePOST the entire TimesheetLines content seems odd.',
         'problem'),
        ('Suggestions very welcome.',
         'outroduction')
    )
})

questions_sentences.append({
    'question_id': 46784,
    'sentences': (
        ('We have developed an integration between our software (a .Net Winforms application) with Xero,\
        allowing the user to import revenue and expense transactions using the API, into our software.',
         'introduction'),
        ('At the moment, every time the user wants to execute this import from within our software, they are presented with a Xero authentication page,\
         where they enter in the username and password, and then on a second page, select the ‘organisation’ they want to allow our software to access\
    (screenshot  https://www.screencast.com/t/JCwxMns3bW8 )',
         'introduction'),
        ('I see that there is an ‘Allow access for 30 mins’ option, which saves them from having to login multiple times, however it still always prompts the user during this 30min period to select the Xero organisation.',
         'problem'),
        ('Is it possible for us to capture and store their Xero username / password, and the organisation that they have originally selected, within our software, so we can programmatically use them in the future?',
         'question'),
        ('So each time they would want to execute an import, they won’t have to login or select their organisation again. Is this possible to do with Xero?',
         'outroduction')
    )
})

questions_sentences.append({
    'question_id': 46210,
    'sentences': (
        ('Our AffinityLive product allows users to record expenses against a project.',
         'introduction'),
        ('In some cases they may not be personal expenses but ones paid for already by a business credit card or chequebook, etc.',
         'introduction'),
        ('We are wondering if these expenses can be pushed through to Xero via the API.',
         'question'),
        ('My understanding is that these are not Expense Claims assigned to a user, but are more general business expenses which are recorded differently.',
         'problem'),
        ('We\'re a bit lost on how to proceed - part of the problem of course is that we\'re not accountants and may be taking the wrong approach!',
         'problem'),
        ('Appreciate any advice.',
         'outroduction')
    )
})


id = 0
for question_sentences in questions_sentences:
    for sentence in question_sentences['sentences']:
        category_id = db.my_query('select training_data_categories_id from training_data_categories where category_name = %s', [sentence[1]])[0][0]
        print('insert into training_data(training_data_id, content, training_data_categories_id, questions_id) values({}, \'{}\', {}, {});'.format(id, sentence[0], category_id, question_sentences['question_id']))
        id+=1
"""

"""
import pyLDAvis.gensim
import gensim
#import graphlab

topics = 100
passes = 20

save_filename = "lda-saves/lda_replies_question_forum_2287_{}_{}".format(topics, passes)

dictionary = gensim.corpora.Dictionary.load(save_filename + ".dict")
corpus = gensim.corpora.MmCorpus(save_filename + ".mm")
ldamodel = gensim.models.LdaMulticore.load(save_filename + ".model")

vis_data = pyLDAvis.gensim.prepare(ldamodel, corpus, dictionary)
pyLDAvis.display(vis_data)
#pyLDAvis.enable_notebook(vis_data)
pyLDAvis.show(vis_data)
"""