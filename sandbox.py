from Database.Configuration import connection_string
from Database.DatabaseHelper import DatabaseHelper

import numpy as np

db = DatabaseHelper(connection_string)

x = []
x.append([3,4])
x.append([3,4])
x.append([3,4])
X = np.array(x)
print(X.shape)


exit()
f = open('questions.txt', 'w')
for row in db.select_query("select question_id, text, content from question where forum_details_id in (select forum_details_id from forum_details where community_id = 0 and name != 'Feature Requests') and question_id not in (select distinct question_id from training_data where question_id not in (125279, 125317,125731,126669,127335,127449,127689,127890,130402,130542,132982,135388,135533,136533,137509,137538,138434,139243,139257,139870)) order by random() limit 160"):
    print(row)
    f.write(str(row[0]) + ", '" + row[1] + "', '" + row[2] + "'\n")
exit()

questions_sentences = []

questions_sentences.append({
    'question_id': 125435,
    'sentences': (
        ('I have just completed my first financial year, and am confused about how to account for Corporation Tax in Xero.',
         'context'),
        ('I have submitted my tax return and just paid the tax due to HMRC.',
         'context'),
        ('I have reconciled the bank transaction so that now I have an Expense sitting against account 500 - Corporation Tax.',
         'context'),
        ('In my Profit and Loss for 2016-17, the expense against code 500 is now shown as an operating expense and reduces down the net profit for the year.',
         'problem'),
        ('Is there any way of separately showing net profit BEFORE tax (and having the Corporation Tax expense sitting between net profit BEFORE tax and net profit AFTER tax?).',
         'question'),
        ('Thanks,Ben',
         'outroduction')
    )
})

questions_sentences.append({
    'question_id': 137779,
    'sentences': (
        ('I have completed all of the payroll enrolment details in Payroll settings but Xero is not selecting any staff to be included in auto enrolment.',
         'problem'),
        ('All of them are eligible by my reckoning but none are selected.',
         'problem'),
        ('On the Employee tab under Eligibility Status the box is greyed out.',
         'problem'),
        ('I am clearly missing something but after assessing this forum and the videos I am no clearer what I am missing.',
         'problem'),
        ('Could somebody suggest what I am missing.',
         'question'),
        ('ThanksAndy',
         'outroduction')
    )
})

questions_sentences.append({
    'question_id': 136222,
    'sentences': (
        ('Hi all.Im a new Xero user and trying to create my first invoice.',
         'context'),
        ("All good except the invoice isn't showing my bank account details so I can get paid by EFT.",
         'problem'),
        ('How can this be added to the standard template?',
         'question'),
        ('I have entered the details into the financial section.',
         'context'),
        ("I have searched the boards here for an answer and can't seem to find one.",
         'context'),
        ('Thanks!',
         'outroduction')
    )
})

questions_sentences.append({
    'question_id': 128095,
    'sentences': (
        ('HI I have been using xero for 6 months and on the whole it is fantastic.',
         'context'),
        ("One thing that i would like to see is the credit invoices issued by suppliers to be able to be manually ticked against a payment rather than allocating it to another invoice.",
         'problem'),
        ('As a lot of our credit notes do not correspond with invoices from the supplier and it then becomes difficult for suppliers to match off our invoices from our remittances.',
         'problem'),
        ('Also the fact that each time you load an invoice onto a supplier that has a credit note, a reminder comes up that there is a credit note available,',
         'problem'),
        ("this in turn seems to stop the flow of creating another bill, as it takes you to that invoice if you dont allocate this credit.",
         'problem'),
        ('Looking forward to your reply',
         'outroduction')
    )
})

questions_sentences.append({
    'question_id': 136180,
    'sentences': (
        ('i just added new expense account, in the drop down list on Expense claim>Current Claim›New Receipt>account',
         'context'),
        ("the list on expense does not include the new expense account i just created.",
         'problem')
    )
})

questions_sentences.append({
    'question_id': 138215,
    'sentences': (
        ('We have had several issues trying to finalize last weeks pay. 40 Staff.',
         'context'),
        ("We have had Marc@Xero replying and we have made comments to him.",
         'context'),
        ('He has to their credit come back to us.',
         'context'),
        ('All be it late and we made our own interpretations.',
         'context'),
        ("We been me and our accountancy vCFO.",
         'context'),
        ('Finally getting last weeks payroll up to day (having to Process through the old system last week.)',
         'context'),
        ('We hit the process button and it is frozen.',
         'problem'),
        ("The button just won't move.",
         'problem'),
        ('We are told there was an update this morning after an issue fot more than 25 staff in payroll.0,',
         'context'),
        ('We have give Marc access.',
         'context')
    )
})

questions_sentences.append({
    'question_id': 135066,
    'sentences': (
        ("Hi,I have reconciled also bank statement for past financial year from 1st April 2015 to 31st March 2016. I usually run monthly profit and loss reports.",
         'context'),
        ("However, for the final month of March the P&L report shows me as final conversion balances for the year ended March 2016 rather than the individual March month income and expenses.",
         'problem'),
        ('Any help and ideas appreciated on this topic. Ash',
         'outroduction')
    )
})

questions_sentences.append({
    'question_id': 135142,
    'sentences': (
        ('I am struggling to sort out the best way to handle reconciling two transactions I have in Xero.',
         'context'),
        ("I have two separate vendors who issued partial refunds after a purchase was made.",
         'context'),
        ('One was because we were charged too much for shipping and the other because we were charged for an upgrade that we did not end up using.',
         'context'),
        ('Both of the original expenses were one off expenses paid via credit card and do not have associated bills.',
         'context'),
        ("They were just reconciled along with other bank transactions.",
         'context'),
        ('How do I handle the refunds?',
         'question'),
        ('They don\'t seem to be overpayments, and I don\'t have a bill to create a credit note against.',
         'problem'),
        ("I could create bills but is that a best practice?",
         'question'),
        ('If I just choose to reconcile it and label is as "vendor refund" is it categorized as an asset or as revenue?',
         'question'),
        ('Any guidance would be very much appreciated. Thanks!',
         'context')
    )
})

questions_sentences.append({
    'question_id': 126593,
    'sentences': (
        ('Hi there — I am starting a business that is pretty straightforward wholesale distribution.',
         'context'),
        ("Payments will mostly come in via check, but many customers will pay via credit card.",
         'context'),
        ('I love the idea of being able to email an invoice to a customer with a big PAY NOW button, which will let them simply input their CC details secureley and pay their invoice.',
         'context'),
        ('This is a new venture for me, though, and I\'m admittedly ignorant on the details and variables I should be considering when making this.',
         'problem'),
        ("Which service should I integrate?",
         'question'),
        ('How do the services that integrate with Xero compare to setting up Merchant Services through my bank?',
         'question'),
        ('Would appreciate any guidance regarding how I might go about thinking about this problem and coming up with a good solution."),',
         'outroduction')
    )
})

questions_sentences.append({
    'question_id': 126082,
    'sentences': (
        ('Hi there,We use Capital On Tap as a regular loans service.',
         'context'),
        ("There is no option for bank feeds and the loan is paid in as and when we require it (almost like a transfer from a separate account with a loan limit).",
         'context'),
        ('We then have to pay back a minimum amount every month depending on the cumulative total we have loaned at the end of that month so the amount is never fixed, always variable.',
         'context'),
        ('I ideally want to record the capital we have received (ad hoc), the amount we have paid back (monthly) and the interest as an expense.',
         'context'),
        ("The loan was started before we began using Xero so I realise I will need to enter a conversion balance.",
         'context'),
        ('But I was wondering if anyone had any idea on how to go about recording the payments in, the repayments out and the interest.',
         'question'),
        ('Would I need to create two accounts, one for loan and one for loan interest?',
         'question'),
        ('I hope this makes sense and thanks in advance for any help or light you can shed on this.',
         'outroduction'),
        ('Many thanks,Joe',
         'outroduction')
    )
})

questions_sentences.append({
    'question_id': 139105,
    'sentences': (
        ('I\'m just starting to reconcile after adding Kounta integration, and am not sure how to handle cash purchases made from the cash register.',
         'context'),
        ("If a supplier is paid cash on delivery from the till, the deducted cash is recorded as \"cash out\" showing the reduced cash in the till.",
         'context'),
        ('How do I record this invoice paid by cash in Xero?',
         'question'),
        ('The Kounta integration only shows the reduced cash in "cash register clearing account", not the COGS account.',
         'problem'),
        ("When you receive a purchase order in Kounta it doesn\'t appear to allow you to specify how the invoice was paid.",
         'problem'),
        ('Thanks,Christie',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 127624,
    'sentences': (
        ('I have been using Xero for a couple of years and absolutely love it.',
         'context'),
        ("However I have a major problem today in that one of my clients is now registered for the Flat Rate Scheme at 12%.",
         'problem'),
        ('When I generate the VAT Return every box is coming up 0.00.',
         'problem'),
        ('Can anyone help ?',
         'question')
    )
})
questions_sentences.append({
    'question_id': 137054,
    'sentences': (
        ('I am currently looking for a quicker and more accurate way to report my super contributions.',
         'context'),
        ("We currently use CBUS clearing account however the CSV file they require every month is not downloadable from Xero.",
         'problem'),
        ('Does anyone else upload a file direct from Xero to a clearing house?',
         'question'),
        ('I tried to use the auto option in Xero through Click Super but as I need receipts to send to customers and neither Click or Xero can offer any reporting this is a dead end.',
         'problem'),
        ("Any suggestions?",
         'question')
    )
})
questions_sentences.append({
    'question_id': 139449,
    'sentences': (
        ('We currently use Xero and are now in the process of finding a suitable POS and Stock control system.',
         'context'),
        ("Ideally the POS system we would like touch screen based suitable for staff with limited computer skills or even iPad as we"
         "    could operate with more than one sales counter Our stock is varied from standard hardware / building lines  through to Animal health and stock feed,"
         "so we need to be able to sell in the same item in different formats. bulk and per metre / or per KG  or single units."
         "We do run monthly accounts for customers as well.",
         'context'),
        ('we previously tried myob retail manager - and it failed as it was far to complex',
         'problem')
    )
})
questions_sentences.append({
    'question_id': 134058,
    'sentences': (
        ('"HiWe have some suppliers who have up to 70 invoices required for paymentTo avoid having to enter these all individually we create one purchase for the supplier,',
         'context'),
        ("and in the body of the purchase, enter all the invoices. Of course we are unable to list every invoice number in the reference box, so we call it by the month of statement.",
         'context'),
        ('It makes it very easy then to identity, pick up & batch all bills that need to be paid at the end of the month, as they all have the same reference.',
         'context'),
        ('This works fine for us, but we do get requests from our suppliers as to what invoices we are paying, as the remittance only says \'April 17 Statement\'.',
         'problem'),
        ("Is there anyway to send a remittance with the body of the purchase showing?",
         'question'),
        ('Are we purchasing incorrectly?',
         'question'),
        ('Thanks',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 138923,
    'sentences': (
        ('Hi,I run a staff temping agency and hire out my staff to other businesses.',
         'context'),
        ("Is there a Xero connected app that allows the clients to approve time-sheets online?",
         'question'),
        ('Thanks',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 134874,
    'sentences': (
        ('Hi, I was asked to run an aged receivables report for 90 days and older (retentions of 5-10%)',
         'context'),
        ("but when I did there were invoices showing up as outstanding but when you drill into them it's been paid and the outstanding amount is $0",
         'problem'),
        ('Has anyone had this issue before?',
         'question')
    )
})
questions_sentences.append({
    'question_id': 125232,
    'sentences': (
        ('"I have been advised by our accountant to put through a number of invoices from a client as a \'bad debt\'.',
         'context'),
        ("I followed the forum posts and set up the account code and put through as credit notes but I'm told this isn't what they want.",
         'problem'),
        ('Is it possible to put through a bad debt differently, such a journal entry, on an accrual scheme so that we can claim the VAT back but still'
         'leave the invoices open in case we do eventually get payments in?',
         'question'),
        ('We want to still be able to send statements etc, if requested, but adding a credit note to the invoices means that we are not able to do this as they\'re down as \'paid\',',
         'context')
    )
})
questions_sentences.append({
    'question_id': 128746,
    'sentences': (
        ('"Hi thereWe don\'t raise Xero invoices for our occasional suppliers, instead we\'ll simply create the transactions at reconciliation time,'
         'adding a new contact as necessary.',
         'context'),
        ("My question is -  what's the easiest way to search for these transactions by contact name?",
         'question'),
        ('I had a case this morning where I needed to quickly add a file to a historical transaction for a known contact and I had to do the following:- Start at the dashboard.'
         '- Click on Accounts -> Bank Accounts- Click the correct bank account.- Click the \'Transactions\' tab.- Click \'Search\', enter the contact name.'
         'Click the appropriate transaction from the list that appears.',
         'context'),
        ('That\'s quite laborious and also involves knowing which bank account the transaction belongs to.',
         'problem'),
        ("What am I missing here?",
         'question'),
        ('I tried, instead, to do it via the \'Contacts\' page, searched and found the correct contact, but there didn\'t seem to be a link to click through and view all'
         'transactions associated with that contact.',
         'problem'),
        ('Frustratingly, I could see a bar graph, visualising the transaction amounts, but no obvious way to view them.',
         'problem')
    )
})

questions_sentences.append({
    'question_id': 135892,
    'sentences': (
        ('Hi,This is a more general question about physical inventory management and not necessarily related to Xero'
         'but I figure that this is probably a good place to ask as I can\'t be the only person selling physical products',
         'context'),
        ("My business is wholesale alcohol business and we have to do regular inventory counts in our multiple warehouses.",
         'context'),
        ('At the moment this is done manually on paper and then transferred to excel.',
         'context'),
        ('I would like to move to a more automated system where the person doing the inventory count scans a product barcode and types in the number of items in the warehouse.',
         'context'),
        ("If this can be achieved with a barcode scanner that links wirelessly to an app on a tablet or phone it would be great.",
         'context'),
        ('I\'ve been trying to find suitable products to do this but haven\'t yet found the right solution.',
         'problem'),
        ('How do other people handle this?',
         'question'),
        ('Are there any hardware / software solutions out there that you would recommend?',
         'question'),
        ('Thanks!Harold',
         'outroduction')
    )
})

for question_sentences in questions_sentences:
    for sentence in question_sentences['sentences']:
        print(sentence[1])
        print(question_sentences['question_id'])
        category_id = db.select_query('select training_data_category_id from training_data_category where category_name = %s', (sentence[1],), fetch_to_dict=False)[0]
        db.insert_query('insert into training_data(content, training_data_category_id, question_id) values(%s, %s, %s)', (sentence[0], category_id, question_sentences['question_id']))

"""#DEVELOPER COMMUNITY DATA
questions_sentences.append({
    'question_id': 45917,
    'sentences': (
        ('Hi,The Australian Payroll API was recently updated to include USI (unique superannuation identifier).',
         'context'),
        ('I have an external system I connect to Xero that tries to match a super fund based on SPIN/USI, and I cannot search by USI via the API. ',
         'context'),
        ('When I to find a Super Fund via the API by querying on the new USI field, and it keeps returning an error "USI property is not supported for Where or Order clause".',
         'problem'),
        ('I can query by other fields e.g. SPIN Example query: /payroll.xro/1.0/SuperFunds?Where=USI%3D%3D%22TLS0100AU%22 ',
         'context'),
        ('API exception returned: USI property is not supported for Where or Order clause',
         'problem'),
        ('Can anyone help?',
         'question')
    )
})

questions_sentences.append({
    'question_id': 46105,
    'sentences': (
        ('I am getting reports from users of an error "Account could not be found" when sending their sales to Xero via the API.',
         'problem'),
        ('It appears that the accounts they are sending to exist, is there anything else that can cause this error?',
         'question')
    )
})

questions_sentences.append({
    'question_id': 46599,
    'sentences': (
        ('Hey!We are looking for a highly experianced developer who has is well versed in Ruby On Rails to intergrate veeqo.com with Xero.',
         'problem'),
        (' So that Veeqo.com clients can export their sales invoices/purchase orders/COGS to Xero.',
         'context'),
        (' Preferably someone who has experience of doing something similar would be great.',
         'context')
    )
})

questions_sentences.append({
    'question_id': 45852,
    'sentences': (
        ('Hi,How do I  set the Branding theme when creating a new invoice using BrandingThemeId?',
         'question'),
        (' How do I find the GUID that is related to the theme I want to use?',
         'question')
    )
})

questions_sentences.append({
    'question_id': 46022,
    'sentences': (
        ('Hi Guys, I just noticed something that might been little strange or also might be by design.',
         'context'),
        ('when creating an invoice i include the contact record details (no guid) full details, this normally either creates a new contact or finds and existing one.',
         'context'),
        ('during testing i noticed that one of the contact matched even thou the company name was different.',
         'problem'),
        ('it then updated the contact and changed the company name.  Edited \t26 Jun 2014 3:20 p.m. \tSystem Generated \tName changed from \'OLD COMPANY\' to \'NEW COMPANY\'.',
         'context'),
        ('personally would have expected the new company to be created not some existing company updated.',
         'problem'),
        ('Can you please let me rules that are used for matching contacts as for some of the records i am processing i might have to create a contact in a separate call and pass in the guid instead.',
         'question'),
        ('particularly if a customer has multiple businesses operating from the same location.',
         'context'),
        ('ThanksPaul',
         'outroduction')
    )
})


questions_sentences.append({
    'question_id': 45787,
    'sentences': (
        ('How can I add the parameter UpdatedDateUTC with the object to Xero? ',
         'question'),
        ('I\'m trying to get invoices from one system to Xero but with the other system\'s modified_dates.',
         'context'),
        ('I\'m adding it with the XML object but it does not seem to make any difference.',
         'problem'),
        (' Example object object:SimpleXMLElement Object(    <Invoice> => SimpleXMLElement Object        (            <InvoiceID> => 4fa68953-c4cc-4c5e-ab64-5e9f38b6e0f5            <Type> => ACCREC            <Contact> => SimpleXMLElement Object                (                    <ContactID> => 85d15bf3-207f-4278-8449-e12dade98c66                )            <Date> => 2015-07-06            <DueDate> => 2015-07-06            <InvoiceNumber> => INV-0031            <CurrencyCode> => USD            <CurrencyRate> => 1.000000000000000            <Status> => AUTHORISED            <SentToContact> => false            <SubTotal> => 59.85            <TotalTax> => 5.24            <Total> => 65.09            <LineAmountTypes> => Exclusive            <UpdatedDateUTC> => 2015-07-06T13:10:46            <LineItems> => SimpleXMLElement Object                (                    <LineItem> => SimpleXMLElement Object                        (                            <AccountCode> => 200                            <TaxType> => TAX001                            <Description> => \'Fish out of Water: Finding Your Brand                            <Quantity> => 3.0000                            <UnitAmount> => 19.9500                            <ItemCode> => BOOK                            <TaxAmount> => 5.236875                            <LineAmount> => 59.85                            <DiscountRate> => 0.0000                        )                )        ))"),\'',
         'code')
    )
})

questions_sentences.append({
    'question_id': 44624,
    'sentences': (
        ('Hi there,At the moment we use the demo environment.',
         'context'),
        ('However have three problems with it.',
         'problem'),
        ('One of them is that it does not contain our production data and the second one is that it expires after 30 days.',
         'problem'),
        ('The third problem is that it is bound to one account, which makes it harder for the developers to share one demo environment to test.',
         'problem'),
        ('Does Xero support a sandbox environment or an environment which is a copy of production?',
         'question'),
        ('Or is it possible to keep the demo environment alive for more then 30 days, including the sharing of the demo account?',
         'question'),
        ('Thanks and Regards,Keethanjan',
         'outroduction')
    )
})

questions_sentences.append({
    'question_id': 46320,
    'sentences': (
        ('I\'m wondering if there is any way to limit the number of results returned--for example, an equivalent to "SELECT TOP 100" in SQL.We intend to create about 800 invoices per month via the API, and all of them will be created on the same day and have the same invoice date and due date, so I don\'t think we could use any date fields or "if modified since" to limit the results.',
         'question'),
        ('  When issuing a GET request on these, ideally, we\'d be able to split it up into 8 different API calls; i.e.',
         'problem'),
        ('in the following pseudo code:\tRequest 1 of 8: Get the top 100 records where invoice date is 2012-04-02T00:00:00 order by UpdatedDateUTC\tRequest 2 of 8: Get the top 100 records where invoice date is 2012-04-02T00:00:00 and UpdatedDateUTC > (the last UpdatedDateUTC in Request 1) order by UpdatedDateUTC\tAnd so on, until there are no more records retrieved.\t',
         'code'),
        ('Is there any way either to limit the records returned or some other way to split up this request into multiple API calls?',
         'question')
    )
})
questions_sentences.append({
    'question_id': 46662,
    'sentences': (
        ('I am looking for a Xero Developer who can create a simple job sheet add-on for my creative company.',
         'problem'),
        ('Will start as a simple job sheet but will no doubt grow into something bigger as my business grows.',
         'context'),
        ('Very keen to discuss with anyone that can help.',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 44469,
    'sentences': (
        ('Hi,I am looking for an integration between Xero and Linnworks',
         'problem'),
        ('We want to be able to exact invoices from Linnworks and pass them to Xero daily through an API integration.',
         'context'),
        ('The invoices passed from the two system will include the following details:1. Invoice Date 2. Invoice Number 3. Contact Name 4. Contact Address 5. Reference Number 6. Product Description 7. Product Quantity 8. Product Price 9. Currency 10. Delivery Cost 11. Sales Account 12. Tax Type',
         'context'),
        ('My client has a budget of £250 to £400 for the work',
         'context'),
        ('ThanksMark',
         'outroduction')
    )
})

"""
"""
questions_sentences.append({
    'question_id': 45062,
    'sentences': (
        ('I find the new .Net library extremely unintuitive and convoluted.',
         'problem'),
        ('Even looking at the example implementations it is not a quick or easy thing to tease out the best way to implement and utilise this myself.',
         'problem'),
        ('I look forward to a straightforward library with straightforward example code of how to implement it.',
         'problem'),
        ('IMHO, 9 arguments for a constructor is too many (see PartnerMvcAuthenticator in the example code).',
         'problem')
    )
})

questions_sentences.append({
    'question_id': 47098,
    'sentences': (
        ('Hello, I\'ve got problem when trying to exchange request token to access token (sending request to /oauth/AccessToken).',
         'problem'),
        ('First step was completed successfuly and I redirected myself to /APIAuthorise.aspx page, where I authorized my app to access my account.',
         'context'),
        ('After redirecting me back to callback url I always get "oauth_problem=signature_invalid&oauth_problem_advice=Failed%20to%20validate%20signature" response from /oauth/AccessToken.',
         'problem'),
        ('Here are data I send and receive:This code is provided by the developer community - Xero does not warrant it in any wayI\'m pretty sure that signature is made correctly -',
         'context'),
        ('I use OAuthSimple class provided in one of Xero`s code samples.',
         'context'),
        ('Full sample works correctly, the problem appears when I try to attach the library into our application.',
         'problem'),
        ('It\'s the newest version available.',
         'context')
    )
})

questions_sentences.append({
    'question_id': 45761,
    'sentences': (
        ('Hi,I am using the Xero API and sending a HTTP GET request from my application to Xero to return Contacts that match a certain Name.',
         'context'),
        ('So...using instructions from http://developer.xero.com/documentation/getting-started/http-requests-and-responses/#title3, I send (for example) Name="A Company Ltd" urlencoded as part of the URL.',
         'context'),
        ('This works fine, until I search on a Name that includes a double quote in it.',
         'problem'),
        ('Does anyone know how to get it to work and Xero to not return an error when a double quote exists?',
         'question'),
        ('I know it\'s highly unlikely that a Name would have a double quote in it, but it\'s always best to make an application as robust as possible in my opinion, no matter how unlikely.',
         'context'),
        ('Many thanks in advance.Cheers,Rhyd.',
         'outroduction')
    )
})

questions_sentences.append({
    'question_id': 45185,
    'sentences': (
        ('I\'m trying to return all Invoices for June 2013, NOT just those that have been changed since a certain date.',
         'context'),
        ('I can see how the API documentation handles this situation, it says to use the following value for the where parameter (from http://developer.xero.com/api-overview/http-requests-and-responses/#get-filtered):',
         'context'),
        ('FullyPaidOnDate >= DateTime(2011, 10, 01) AND FullyPaidOnDate <= DateTime(2011, 10, 30)',
         'code'),
        ('However I\'d like to use the useful xero.php wrapper if possible.',
         'problem'),
        ('After reading the github page and various discussions on here as well as the code, it looks to me as if the filter I should be setting is as follows (ie the \'value\' of the array item is itself an array made up of operand, literal value):',
         'context'),
        ('$aFilter = array(\t\'Date\' => array(\'>=\',\'DateTime(2013, 06, 01)\')\t,\'Date\' => array(\'<=\',\'DateTime(2013, 06, 30)\'));$result = $xero->Invoices(\'\',\'\',$aFilter,\'\');',
         'code'),
        ('However this results in the following error:Array(    [ErrorNumber] => 16    [Type] => QueryParseException    [Message] => Operator \'<=\' incompatible with operand types \'DateTime?\' and \'String\')',
         'problem'),
        ('Also of course as the field name is the array key, I only end up with one array item not two as you can see in the array dump:',
         'problem'),
        ('Array(    [Date] => Array        (            [0] => <=            [1] => DateTime(2013,06,30)        ))',
         'code'),
        ('Any help that you can offer would be appreciated.',
         'outroduction')
    )
})

questions_sentences.append({
    'question_id': 46680,
    'sentences': (
        ('Dear Sirs,This question is targeted toward Xero support people and administrators.',
         'context'),
        ('I was not able to find answer to my question, so I have to post my question here.',
         'context'),
        ('COZYROC is the leading provider of third-party components for Microsoft SQL Server Integration Services.',
         'context'),
        ('We have recently included adapters which support the Xero application.',
         'context'),
        ('We would like to ask what information you need from us so you can post details about COZYROC\'s solution here:https://developer.xero.com/code-samples/tools/overview/',
         'question'),
        ('Thank you for your time in advance!',
         'outroduction')
    )
})

questions_sentences.append({
    'question_id': 45763,
    'sentences': (
        ('Hi all. I\'m a newbie web developer and also new to xero api.',
         'context'),
        ('What I am asking is simple. How to create the function for a GET/POST request for invoices?',
         'question'),
        ('I have looked at the api previwer, understand the xml but not how to implement the "run" button function',
         'problem'),
        ('Any sample code to look at including a submit button?',
         'question')
    )
})

questions_sentences.append({
    'question_id': 44963,
    'sentences': (
        ('I have been uploading Timesheets to Xero successfully in an application in C# for over 12 months.',
         'context'),
        ('With the latest revision of the app (no changes to the codeline used for the Timesheets upload), I am no longer able to do the uploads and am getting a BadRequest exception raised.',
         'problem'),
        ('The detail merely shows "A validation exception occurred".',
         'problem'),
        ('I have the Api.Timesheets.Create in a try/catch block, with three separate catch blocks.',
         'context'),
        ('The first of these is:catch (Xero.Api.Infrastructure.Exception.ValidationException vE){.....}but this is not trapping.',
         'problem'),
        ('The second catch block is for BadRequestException and that traps.',
         'context'),
        ('How can I then determine the actual Validation errors?',
         'question'),
        ('The full ValidationException block contains::\terrStore += "Validation errors from xero:\\r\\n";\tforeach (var v in vE.ValidationErrors)\t{\t\terrStore += v.Message + "\\r\\n";\t\tAppGlobals.logger.Error("Error: TS Upload error" + v.Message + "\\r\\n");\t}',
         'problem'),
        ('but with that not being trapped how can I find the errors?',
         'question'),
        ('Why does the BadRequest exception supersede the ValidationException, or are there multiple exceptions occurring?',
         'question'),
        ('It makes life fairly difficult when my client cannot determine what has gone wrong without my having to get into debug mode on a production system.',
         'problem'),
        ('Eric Whitchurch',
         'outroduction')
    )
})

questions_sentences.append({
    'question_id': 46916,
    'sentences': (
        ('Hi,I would like to know if there is a way to force expire the token?',
         'question'),
        ('I want to test my application against different scenarios so it will be great if we can "induce" token expiration instead of having to wait 30 minutes for it to systematically expire.',
         'problem'),
        ('I am using a public application and official PHP Xero API wrapper.',
         'context'),
        ('Thanks!',
         'outroduction')
    )
})

questions_sentences.append({
    'question_id': 44426,
    'sentences': (
        ('Why is it that Xero will not accept an email address with numeric characters in the TLD either by API or manual Contact entry?',
         'question'),
        ('There are TLDs which have numeric character in them listed on IANA - http://data.iana.org/TLD/tlds-alpha-by-domain.txt  (scroll down to .XN domains).',
         'context'),
        ('(encoded as "xn--mgberp4a5d4ar") ("al-Saudiah") in Arabic Script,which is registered to the Saudi Network Information Centre',
         'context'),
        ('I get thrown this error via API:Error: 10 ValidationException A validation exception occurred Email address must be valid. Email address must be valid.',
         'problem'),
        ('Thanks.',
         'outroduction')
    )
})

questions_sentences.append({
    'question_id': 46159,
    'sentences': (
        ('Hi,I have a web app that requires invoicing, inventory and payroll access to insert timesheets.',
         'context'),
        ('Have got it working using the core api Version 2 & have got hold of the payroll DotNet sample (which looks to be the same as the core api sample with a console payroll section).',
         'context'),
        ('Anyway the example doesn\'t show the situation where I wan to use both api\'s...i.e I want to process invoices using the core api and then turn the page to payroll and insert time-sheets.',
         'problem'),
        ('Do I have to log out of 1 and log into the other?',
         'question'),
        ('Can I use the same access token to create both payroll and core repositories?',
         'question'),
        ('Any examples of the above in DotNet?',
         'question')
    )
})
"""


"""
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
         'context'),
        ('We have different versions of same product running on cloud . each client has its own url like https ://<<clientname>>.ourproduct.com.',
         'context'),
        ('Will you please suggest what app type we should use ?',
         'question')
    )
})

questions_sentences.append({
    'question_id': 45329,
    'sentences': (
        ('Hi GuysI did a quick search for this but couldn\'t find an answer I was looking for. The documentation describes:  "Daily Limit: 5000 calls in a rolling 24 hour window"',
         'context'),
        ('We have different versions of same product running on cloud . each client has its own url like https ://<<clientname>>.ourproduct.com.',
         'context'),
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
         'context'),
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
         'context'),
        ('There were at least 3 possible places this question could\'ve been created, but I figured as I\'m using wrapper code it should go here.',
         'context'),
        ('I\'m using the .NET Xero API SDK 2.0.20 in C#.I\'m trying to send an invoice to a customer upon payment.',
         'context'),
        ('It should be sent with the invoice in a paid state (so there is no confusion).',
         'context'),
        ('I\'ve got the code down good to apply the payment to the invoice, and sending the e-mail goes fine.',
         'context'),
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
         'context'),
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
         'context'),
        ('At the moment, every time the user wants to execute this import from within our software, they are presented with a Xero authentication page,\
         where they enter in the username and password, and then on a second page, select the ‘organisation’ they want to allow our software to access\
    (screenshot  https://www.screencast.com/t/JCwxMns3bW8 )',
         'context'),
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
         'context'),
        ('In some cases they may not be personal expenses but ones paid for already by a business credit card or chequebook, etc.',
         'context'),
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