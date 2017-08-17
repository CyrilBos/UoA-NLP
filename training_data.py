from Database.Configuration import connection_string
from Database.DatabaseHelper import DatabaseHelper

import numpy as np

db = DatabaseHelper(connection_string)


def update_db(questions_sentences):
    for question_sentences in questions_sentences:
        already_in_db = db.select_query('select * from training_data where question_id = %s',
                                        (question_sentences['question_id'],))
        if len(already_in_db) == 0:
            for sentence in question_sentences['sentences']:
                print(sentence)
                category_id = \
                    db.select_query(
                        'select training_data_category_id from training_data_category where category_name = %s',
                        (sentence[1],))[0]
                db.insert_query(
                    'insert into training_data(content, training_data_category_id, question_id) values(%s, %s, %s)',
                    (sentence[0], category_id, question_sentences['question_id']))


def get_new_training_data(number, community='Business', save_filename=None):
    if save_filename:
        f = open(save_filename, 'w')
    for row in db.select_query("select question_id, text, content from question where forum_details_id in (select forum_details_id from forum_details where community_id = {} and name != 'Feature Requests') and question_id not in (select distinct question_id from training_data) order by random() limit {}".format(db.get_community_id(community)[0],number)):
        print(row)
        if save_filename:
            f.write(str(row[0]) + ", '" + row[1] + "', '" + row[2] + "'\n")

questions_sentences = []

questions_sentences.append({
    'question_id': 125279,
    'sentences': (
        ('hi just wondering if anyone knows how to deal with eftpos cash outs in xero',
         'context'),
        ('so we  have a small cafe some times we do eftpos cash outs for our customers which is paid back to us the same day when we do our eftpos settlement ,when the eftpos settlement show up in xero from our bank feed it includes all eftpos transactions for that day and the cash out eg 500 income plus 20 cash out total 520 i code the 500 to income and have been coding the cash out to income non gst (eftpos cash out )',
         'context'),
        ('but im not sure how to show that it has been paid to the customer as it comes from the till when we do the cash banking for that day the bankings are down 20 because of the cash out eg banking should be 300 but is less 20 from cash out given so when the bank feed comes through for the banking it shows as 280 should i just note on that day that there was a 20 cash out given it does balance mabe im over thinking it a bit...',
         'problem'),
        ('might be easier to keep a manual diary of cash paid / cash out',
         'problem'),
        ('any ideas',
         'outroduction')
    )
})

questions_sentences.append({
    'question_id': 125317,
    'sentences': (
        ('Hello, Sorry if this is already somewhere. ',
         'context'),
        ('I need help recording payment fees deducted from income. ',
         'context'),
        ('I have sales invoices with -Services-Product SalesCash and Card payments received are then applied to the sales invoice. ',
         'context'),
        ('However, 20% of card transactions are deducted before it is sent to us for a cash advance, so these fees somehow need to be recorded as Loan Repayments. ',
         'problem'),
        ('Also, Stripe payments are also applied to the invoice as payment recieved but a fee is deducted before we receive it, ideally these need to be recorded as Merchant Fees. ',
         'problem'),
        ('Is there a simple way of doing this? ',
         'question'),
        ('I am going round in circles and not really getting anywhere.',
         'context'),
        ('Many thanks,',
         'outroduction'),
    )
})

questions_sentences.append({
    'question_id': 125731,
    'sentences': (
        ('Hi,For one of my bank accounts, the live feed is operating and I have checked that the transactions are pulling through as per my bank statement, however the account balance differs from the bank statement. ',
         'problem'),
        ('Refreshing the feed does not seem to help either. ',
         'context'),
        ('Please can anyone provide help on how to fix this? ',
         'question'),
        ('Thanks. ',
         'outroduction'),
    )
})

questions_sentences.append({
    'question_id': 126669,
    'sentences': (
        ("Hi, I'm a newbie so forgive me if this is something really obvious that I'm missing but after a whole day of searching help, I don't seem to be able to find the answer.",
         'context'),
        ('I have a balance that is incorrect, even after going through and checking all of the transactions, so I wanting to check the running balance to see where it was going wrong - I went to reports to do this. ',
         'problem'),
        ('I selected the transaction details for the first month of my accounts and the start balance was correct but the end of month balance was wrong. ',
         'context'),
        ('I then realised that all my spending is under the top heading of credit and all my income is under debit. ',
         'context'),
        ('When I total the columns as they should be and add and subtract these from my opening balance I get the same balance as my bank statement, but on Xero it\'s not working.',
         'problem'),
        ('Can anyone help? ',
         'question'),
        ('Thanks',
         'outroduction'),
    )
})

questions_sentences.append({
    'question_id': 127335,
    'sentences': (
        ("If a supplier is not registered for GST (has ABN, doesn't charge GST) - what tax code should be used when entering their invoice? ",
         'question'),
        ('Should I set up a different tax code at 0% - I want to make sure the expenses still end up on the BAS. ',
         'question'),
    )
})

questions_sentences.append({
    'question_id': 127335,
    'sentences': (
        ("If a supplier is not registered for GST (has ABN, doesn't charge GST) - what tax code should be used when entering their invoice? ",
         'question'),
        ('Should I set up a different tax code at 0% - I want to make sure the expenses still end up on the BAS. ',
         'question'),
    )
})

questions_sentences.append({
    'question_id': 127449,
    'sentences': (
        ( "Hello everyone, I'm having a problem calculating sales taxes for meals and entertainment in Canada. ",
         'context'),
        ('Sales tax is only claimable on 50% of the sales tax paid for GST/PST purposes in Canada. ',
         'context'),
        ('So, giving a very basic example, if a meal costs 100$ and GST was 5% (ie. 5$), then only 2.50$ can be claimed for GST purposes and the other 2.50$ gets added back to the meals & entertainment expense. ',
         'context'),
        ('Now, in Xero I created a separate sales tax component for meals & entertainment whereby the sales tax rate used for meals and entertainment expenses is half of the GST/PST rate, but this is where I run into problems. ',
         'context'),
        ('In Quebec, GST is 5% and QST is 9.975%. ',
         'context'),
        ('If I have a meal that\'s:Before tax: 5.50$GST @ 5%: 0.28$QST @ 9.975% : 0.55$Total after tax: 6.33$',
         'context'),
        ('The problem is, when I create a sales tax component for GST @ 2.5% and QST @ 4.9875% (which is half of the actual rates), the sales taxes being calculated are not half, since the pre-tax amount that Xero calculated is incorrect. ',
         'problem'),
        ('Xero gives me this:Before tax: 5.89$GST @ 2.5%: 0.15$ (in actuality it should be 0.14$)QST @ 4.9875%: 0.29$ (in actuality it should be (0.27$)Total after tax: 6.33$. ',
         'problem'),
        ("As you can see, when Xero backs out the taxes, the pre-tax rates are different and I'm not able to accurately calculate the sales tax for meals & entertainment expenses, which are supposed to be only claimed at 50%. ",
         'problem'),
        ('Does anyone have a solution? ',
         'question'),
        ("If I'm not being clear please let me know. Thanks. ",
         'outroduction'),
    )
})

questions_sentences.append({
    'question_id': 127890,
    'sentences': (
        ("I've been using the Xero Touch (iOS) to send invoices to customers. ",
         'context'),
        ("When I log into Xero and look at my invoices, the history clearly states that they have been sent, however in the summary screen they are listed as 'invoice not sent' and thus no reminders have been sent. ",
         'problem'),
        ('This is quite frustrating, and is clearly a bug between the iOS app and the webapp. ',
         'problem'),
        ('Is there a solution to this? ',
         'question')
    )
})

questions_sentences.append({
    'question_id': 130402,
    'sentences': (
        ('Currently entering a new bill in purchases 1. Load line with description 2. Manually allocate a portion to a tracing detail 3. Repeat steps 1. and 2. in the same bill to apportion the same item to various tracking details. ',
         'context'),
        ('e.g. Energy bills each month need to be split across various product lines to show the actual costs incurred for each area of the business.',
         'context'),
        ('We use the P&L Report to show in real time the costs incurred to each product line. ',
         'context'),
        ('This information in turn assists in budgeting/ P&L analysis and third party information requests by confirm costs the real time. ',
         'context'),
        ('In our case currently we are manually loading the same item 6 times to get access to this information. ',
         'context'),
        ('Many bills have multiple items which all need splitting, to gain the detail we require.',
         'context'),
        ('Suggestion 1. Load line with description 2. A similar function to the "bank rules reconcile" be added.',
         'problem'),
        ('* The allocated ratios would link to the "Tracking function" rather than "Account"',
         'context'),
    )
})

questions_sentences.append({
    'question_id': 130542,
    'sentences': (
        ("I would like to be able to switch on an 'advanced invoice' setting so that along with the 'invoice date' and 'due date' you can select a 'journal to' date when entering invoices.",
         'problem'),
        ('When you save the invoice, this would then create the relevant journal entries to re-allocate the expense/income to the requested month (leaving VAT entries where they are).',
         'context'),
    )
})

questions_sentences.append({
    'question_id': 132982,
    'sentences': (
        ('I love the expense claim feature in Xero touch except that the users cannot submit a claim. ',
         'problem'),
        ('It would be great if that could be done from IOS or Android and those users would not need to login to a computer at the office. ',
         'context'),
        ('They could do all they need to do from their iPhone.',
         'context'),
        ('Users love taking photos of their receipts on their iPhone but often forget to open the full Xero later in a computer to submit the claim and claims are being missed. ',
         'problem'),
        ('It would be great if they could snap a photo and submit and then the accounts department could do the rest.',
         'context'),
    )
})

questions_sentences.append({
    'question_id': 135388,
    'sentences': (
        ("I have been trying to update the bank feed for the last two days (myself and my colleague have tried on two accounts) and it says that it is refreshing but when it's finished no new transactions are added, yet looking at our Lloyds online banking I can see lots of new payments that haven't been imported, ",
         'problem'),
        ('I have tried a good 5 times already today with the same result each time',
         'context'),
    )
})

questions_sentences.append({
    'question_id': 135533,
    'sentences': (
        ('Hello, I am wondering if somebody can please help me. ',
         'context'),
        ('I need to reconcile balance transfers between the business current account and the business reserve account. ',
         'context'),
        ('Please, do you know which account should I use to reconcile? ',
         'problem'),
        ('Thank you very much for your help Edita',
         'outroduction'),
    )
})

questions_sentences.append({
    'question_id': 136533,
    'sentences': (
        ('I am a new Xero user and I am a bit confused.',
         'problem'),
        ('I have a 50000 EUR bill, and I made a prepayment (overpayment) to my supplier in both EURO and USD currencies.',
         'context'),
        ('Now, I want to use my USD overpayment to credit this bill, but Xero only shows up same currency overpayments.',
         'problem'),
        ('How should I make it work? ',
         'question'),
        ('Thanks! ',
         'outroduction'),
    )
})

questions_sentences.append({
    'question_id': 137509,
    'sentences': (
        ('How is it when you view your payslips and it shows your SGC but is not deducted from their net pay? ',
         'problem'),
        ('Am I doing something wrong? ',
         'question'),
        ('Is it because it shows pending? ',
         'question'),
        ('So does that mean we manually subtract it from their net pay. ',
         'question'),
        ('But in doing that it will show a wrong amount for payment. ',
         'problem'),
        ('Need help!!!',
         'outroduction'),
    )
})

questions_sentences.append({
    'question_id': 137538,
    'sentences': (
        ("Hey all,I have an interesting situation. ",
         'context'),
        ('I have two employees who are married. ',
         'context'),
        ('One has taken a lot more leave than the other (visiting the homeland). ',
         'context'),
        ('The one with less leave is going away again, and will be at -62 hours after it is applied. ',
         'context'),
        ('Is there a way for the employee with lots of leave, to transfer leave to the other one? ',
         'problem'),
        ('They wish to do this and I don\'t see any reason why not. ',
         'context'),
        ('Another situation is if an employee wanted to trade in some leave for cash... ',
         'problem'),
        ('I wouldn\'t be opposed to this and have done it in the past... ',
         'context'),
    )
})

questions_sentences.append({
    'question_id': 139243,
    'sentences': (
        ('We are trying the new Shopify Xero integration app. ',
         'context'),
        ('The app places all Shopify orders into a single account, but we would like it to place orders into different accounts depending on product type or sales channel',
         'problem'),
        ('We have also tried the CarryTheOne solution and it doesnt seem to do it either.',
         'context'),
        ('Are there any Shopify integration apps that allow filtering of orders as they are imported? ',
         'question'),
    )
})

questions_sentences.append({
    'question_id': 139257,
    'sentences': (
        ("I like the principle of being able to use standard MS tools such as Excel to manipulate data and extend the use of Xero. ",
         'context'),
        ("Spotlight is nice for Business Intelligence views but I am a small business that the costs can't carry. ",
         'context'),
        ('I am particularly interested in Moving Annual Averages to provide a normalised view of activity as I operate in the highly seasonal tourist arena. ',
         'context'),
        ('Is there an ODBC link available to connect Excel to the Xero gl balances data tables? ',
         'question'),
    )
})

questions_sentences.append({
    'question_id': 139870,
    'sentences': (
        ("Hi - Ive been really disappointed lately with the length of time that it takes for the support team to respond and then give advice about issues. ",
         'problem'),
        ('Our company deals with other similar organisations and the turn around time is far less. ',
         'context'),
        ('This is really important to us because sometimes a quick question can delay progression of a task. ',
         'context'),
        ('One of the selling points for us was the previous quick turn around from contacting support to getting a response - we thought it was great. ',
         'context'),
        ('Lately we get an email stating they will be in touch within 24 hours, at times it has been longer than this, and then the response has been an auto generated link to a site that usually doesn\'t answer the question. ',
         'problem'),
        ('Personal service is really, really important.',
         'context')
    )
})

questions_sentences.append({
    'question_id': 139107,
    'sentences': (
        ('Hi,I have a client in the fuel distribution industry. ',
         'context'),
        ('They purchase their fuel in bulk and then, after paying for the respective fuel levies and duties that apply for the particular country, they manufacture into a finished product the fuel available for bulk delivery to their customers. ',
         'context'),
        ('Has anyone got a cheaper manufacturing add-on their can recommend other than those available in cin7, unleashed or dear inventory as it is a very simple manufacturing process that does not need a highly complex solution. ',
         'question'),
    )
})

questions_sentences.append({
    'question_id': 126915,
    'sentences': (
        ("I have a Paypal bank acnt on my dashboard for my online sales. ",
         'context'),
        ('I also have my business acnt for my day to day business.',
         'context'),
        ('It looks as though after I have reconciled the acnts they are both treated as one in terms of reporting etc. ',
         'problem'),
        ('Is this the case? ',
         'question'),
        ("So it's like they are separate acnts for the purposes of paying and receiving funds but they are collated as a whole in terms of the reports etc.",
         'question'),
        ('Hope that makes sense :-) Thanks',
         'outroduction'),
    )
})


questions_sentences.append({
    'question_id': 140029,
    'sentences': (
        ('URGENTI am absolutely appalled at the service provided by Xero.',
         'context'),
        ('I have been asking for a call, and nobody will call.',
         'problem'),
        ('Xero claims, they are happy to call you.',
         'context'),
        ('I disagree.',
         'context'),
        ('I have asked 3 times now, and you will not.',
         'context'),
        ('Please call 07740306490 and help my bookkeeper.',
         'context'),
        ('Thank you',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 125719,
    'sentences': (
        (
            'Hello,  I need to set up a Dishonoured Payment account in my chart of accounts to record the fraudulent \"receive money\" transaction from our customer and the bank retrieval \"spend money\" transaction.',
            'context'),
        ('Can anyone please help with where I set this account up in my chart of accounts.',
         'question'),
        ('thanksKathryn',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 134108,
    'sentences': (
        ('When I import bills in Purchases it works fine but it doesn\'t update the cost in Inventory.',
         'problem'),
        ('Is this by design or is there a way to allow this.',
         'question'),
        ('Otherwise I have to manually maintain my inventory costs.',
         'context'),
        ('I have read what I can and searched the forum but can\'t find any info on this',
         'context'),
        ('Anyone know an answer?',
         'question'),
        ('Thanks, Richard',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 136387,
    'sentences': (
        ('Hi All,I use Box (www.box.com) extensively for cloud based storage.',
         'context'),
        (
            'It would be great if there was an option to Export a PDF of any report to your Box account from the Export Button (Currently there are options for PDF, Excel and Google Docs only).',
            'context'),
        ('Now I have to export to PDF, Save to my desktop then drag into Box.',
         'problem'),
        (
            'I know you can publish reports in Xero, but I generally only publish final documents, not reports I use for working papers etc.',
            'context')
    )
})
questions_sentences.append({
    'question_id': 129000,
    'sentences': (
        ('Hi all.',
         'context'),
        ('I\'m looking for something that will use my client list out of Xero.',
         'context'),
        ('I need it to do email merge...',
         'context'),
        ('Anyone recommend anything?',
         'question')
    )
})
questions_sentences.append({
    'question_id': 137078,
    'sentences': (
        ('I\'m trying to find a definitive answer but had no luck.',
         'context'),
        ('My employer wants me to be able to pay employees direct from zero without accessing online banking.',
         'context'),
        ('It doesn\'t seem to be an option.',
         'problem'),
        ('Can anyone confirm?',
         'question')
    )
})
questions_sentences.append({
    'question_id': 138758,
    'sentences': (
        ('If you are a user of Xero and Fergus, tell us how you are getting on and your experience so far.',
         'context'),
        ('Any tips?',
         'question'),
        ('Intuitive job management software designed for tradesmen by tradesmen. ',
         'context'),
        ('Quotes, schedules, invoices, timesheets, GPS tracking and seamless integration, check out .',
         'context')
    )
})
questions_sentences.append({
    'question_id': 126491,
    'sentences': (
        ('Has anyone out in the Xero Community done a large scale change to their chart of accounts?',
         'question'),
        ('We are planning a large change, and just curious to see how others might have tackled it.',
         'context'),
        (
            'I wanted to keep an original \"copy/backup\" of our data up to 12/31/2015 and then roll over a new copy/database for 2016 and make the changes there.',
            'context'),
        ('However, Xero doesn\'t work similarly to QB, where you can download a copy of the database and store.',
         'context'),
        (
            'It was suggested to do a major upload of the new GL codes, however - that seems fraught with issues and potential overwriting, and less out of our control, if you are switching codes one by one.',
            'problem'),
        ('Thoughts?',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 138412,
    'sentences': (
        ('If you are a user of Xero and Zenoti, tell us how you are getting on and your experience so far.',
         'context'),
        ('Any tips?',
         'question'),
        (
            'A cloud-based, all-in-one software solution used by spas, salons and medi-spas to manage and grow their business.',
            'context'),
        ('For more information, check out .',
         'context')
    )
})
questions_sentences.append({
    'question_id': 138540,
    'sentences': (
        ('If you are a user of Xero and EMAC, tell us how you are getting on and your experience so far.',
         'context'),
        ('Any tips?',
         'question'),
        (
            'Intelligent real time job management and billing tool to keep track of jobs, quotes, monitor profit margins as well as add labour time and materials.',
            'context'),
        ('For more information, check out .',
         'context')
    )
})
questions_sentences.append({
    'question_id': 138744,
    'sentences': (
        ('If you are a user of Xero and e360, tell us how you are getting on and your experience so far.',
         'context'),
        ('Any tips?',
         'question'),
        (
            'e360 is an integrated website platform for SME\'s including Content Management, Ecommerce, Email Marketing, CRM, Reports, API & Xero integration, check out .',
            'context')
    )
})
questions_sentences.append({
    'question_id': 127310,
    'sentences': (
        ('I have to post in journals for a client payroll but the site won\'t allow me.',
         'problem'),
        (
            'The charter of accounts shows \'wages payable\' as locked and automatically updated through the software\'s pay run facility(which we are not using).',
            'context'),
        ('Is there any way to unlock this?',
         'question')
    )
})
questions_sentences.append({
    'question_id': 133835,
    'sentences': (
        ('Xero currently isn\'t recording the expense part of salary sacrifice transactions correctly.',
         'problem'),
        ('At present the pre sacrifice amounts allocated to gross wages.',
         'context'),
        ('I would expect the sacrificed amount should be allocated to the appropriate expense.',
         'context'),
        (
            'For example where there is a gross wage of $1200 and $200 sacrificed for superannuation the gross wage of $1200 goes to wages expense and none of the sacrifice to superannuation expense.',
            'context'),
        ('This means each month/quarter/year manual journals are needed to correct the allocation.',
         'context'),
        ('This becomes more important with other types of salary sacrifice, such as motor vehicles where GST applies.',
         'context'),
        (
            'It would be good to add an expense account to pre tax deduction pay items that auto posts the debit to the appropriate expense and credit to the wages expense account.',
            'context'),
        (
            'Alternatively if we have the option for the account in the payroll item to be more than just a liability account as is presently the case.',
            'context'),
        ('This would at least allow the credit entry to be allocated against wages.',
         'context'),
        ('This would then shows correct gross wages and allow the salary sacrifice expense to be managed separately.',
         'context')
    )
})
questions_sentences.append({
    'question_id': 135171,
    'sentences': (
        ('Hi guys!',
         'context'),
        (
            'I have a New Zealand Invoice (I am in Australia) that I have just paid via Forex (so in AUD into a Forex bank account here in Australia).',
            'context'),
        ('How on earth do I enter that into Xero?',
         'question'),
        ('Any advice would be appreciated!',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 125631,
    'sentences': (
        ('We are a builder and have a large number of small invoices from wholesalers.',
         'context'),
        ('These we pay in two or more large payments.',
         'context'),
        (
            'However they often do not match exactly to a certain number of invoices, can you part allocate a payment to an invoice, leaving a remaining balance to clear off with the next invoice.',
            'question')
    )
})
questions_sentences.append({
    'question_id': 138036,
    'sentences': (
        ('i cannot find any option to process an employee leaver and therefore produce a P45 document?',
         'problem'),
        ('any help much appreciated',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 136169,
    'sentences': (
        (
            'I like to run my eye down the account transaction to make sure that ever transaction has an invoice attachment.',
            'context'),
        (
            'The problem is if you create a bill and reconcile it, it doesn\'t register that there is an attachment unless you click on the invoice in the description.',
            'problem'),
        (
            'Having to go through two or three windows to make sure every transaction has an attachment can take a lot of time.',
            'context'),
        (
            'Is there a way for the account transaction page to register the bill that has been reconciled with that transaction has an attachment?',
            'question'),
        ('Thanks',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 136875,
    'sentences': (
        (
            'I have just used payroll for the first time, and on my first pay run, the PAYG YTD is double the amount it should be.',
            'problem'),
        ('It is the first pay so it should be the same as \'This Pay\' column.',
         'context'),
        ('What have I don\'t wrong, or how can i fix this.',
         'question'),
        ('Many thanks',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 134325,
    'sentences': (
        ('We have off-site staff with debit cards.',
         'context'),
        ('We have set them up as Users with the  \"Invoice Only- Invoice=Purchases Only\" user role.',
         'context'),
        (
            'They need to be able to access Spend Money in order to take pictures of their receipts and code to gl accounts for their debit card purchases.',
            'context'),
        ('The mobile app is not showing the + (plus) sign to access spend money.',
         'problem'),
        ('We obviously do not want to provide greater levels of access to the staff.',
         'context'),
        (
            'Is anyone using the mobile app/Spend Money with off-site staff and what User role have you had to assign to accomplish this?',
            'question')
    )
})
questions_sentences.append({
    'question_id': 125724,
    'sentences': (
        ('Hi,our year end was 31st December 2016.',
         'context'),
        ('I have a conversion balance in opening stock from 31st December 2015.',
         'context'),
        ('No other adjustments to stock have been made for the year 2016 so it has a YTD value of 0.00.',
         'context'),
        ('We don\'t use the inventory within Xero as it doesn\'t suit our business needs.',
         'context'),
        ('I have a figure for closing stock and am not sure where to journal the figures from / to.',
         'context'),
        ('My logic would be to leave the opening stock figure as it is.',
         'context'),
        ('Then credit my direct costs and debit closing stock with our closing stock figure?',
         'question'),
        ('I\'m a bit confused with how to handle this in Xero.',
         'context'),
        ('Sage seemed more straightforward :/',
         'context'),
        ('Any advice would be appreciated.',
         'outroduction'),
        ('Many thanks',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 140153,
    'sentences': (
        ('Hi, Got a serious issue this morning when trying to open old files uploaded in AP by receipt bank.',
         'context'),
        (
            'I don\'t know what happened but since the big file rollout but I cannot open, view nor download most of old files uploaded by receipt-bank.',
            'problem'),
        ('Also tried in chrome and nothing.',
         'context'),
        ('Scary.',
         'context'),
        ('Please confirm you guys are working on this to fix it ASAP.',
         'question'),
        ('Thanks.',
         'outroduction'),
        ('Otherwise, I just love the new file feature !',
         'context'),
        ('keep up the good work',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 127017,
    'sentences': (
        ('I have searched the FAQs but can\'t find the instructions.',
         'context'),
        ('Can anyone please help?',
         'question'),
        ('Thanks.',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 128073,
    'sentences': (
        ('Can the batch payment report please list the payments in the order they are in the batch?',
         'question'),
        ('I sorted a batch by supplier, however the PDF has them listed in a seemingly random order.',
         'problem'),
        (
            'I provide the original invoices with the payment batch for tick off and it is easier if they are sorted alphabetically.',
            'context')
    )
})
questions_sentences.append({
    'question_id': 138438,
    'sentences': (
        ('If you are a user of Xero and Progressclaim.com, tell us how you are getting on and your experience so far.',
         'context'),
        ('Any tips?',
         'question'),
        ('Progressclaim.com, submit construction progress claims online, from any device, in seconds.',
         'context'),
        (
            'Xero invoices created instantly with professional and compliant claims documentation attachedFor more information, check out .',
            'context')
    )
})
questions_sentences.append({
    'question_id': 127996,
    'sentences': (
        ('How do I set up an account for Discounts received from suppliers and what type please.',
         'question'),
    )
})
questions_sentences.append({
    'question_id': 126511,
    'sentences': (
        ('Has anybody had experience accounting for Groupon deal payments in Xero?',
         'question'),
    )
})
questions_sentences.append({
    'question_id': 126094,
    'sentences': (
        (
            '\'Hi All,It would appear that when I run reports such as profit & loss that it calculates the sales etc when the invoice was dated and not when payment is received.',
            'problem'),
        ('Is it possible to change the settings so that the sale is added into the period when payment is received?',
         'question'),
        ('Any help would be appreciated.',
         'outroduction'),
        ('Cheers',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 126263,
    'sentences': (
        (
            'Hiya, new to Xero and having a few issues, can anyone please advise me:I have bank fed and reconciled my accounts so that they balance.',
            'context'),
        (
            'Do I now need to add in company receipts and invoices paid to bills, or am I just repeating the process that reconciling does??',
            'question'),
        ('if so what is the point in having \"Bills you need to pay\"',
         'question'),
        ('Thanks in advance',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 128987,
    'sentences': (
        (
            'We love to hear how business owners are working with their accountant or bookkeeper beyond traditional compliance work.',
            'context'),
        ('Share stories of what you\'ve been doing with your advisors now you\'re collaborating together on Xero.',
         'question')
    )
})
questions_sentences.append({
    'question_id': 135470,
    'sentences': (
        (
            'When trying to edit invoices and quotes, the \"reference number\" on the invoice/quote keeps coming up as the invoice number.',
            'context'),
        (
            'e.g. Invoice No. - INV-0019Reference should be - \"customers name\"but it comes up as INV-0019I went onto the .docx file but it shows the <<invoiceNumber>> where the invoice number is and <<reference>> where reference is.',
            'problem'),
        ('Any ideas?',
         'question')
    )
})
questions_sentences.append({
    'question_id': 134177,
    'sentences': (
        ('This Xero  shows the process of entering receipts.',
         'context'),
        (
            ' It starts with the mobile app, and then moves to the browser and at 50 seconds says \"just like the mobile app fill in the expense\".',
            'context'),
        ('Except from what I can see, it\'s not just like the mobile app.',
         'context'),
        (
            'In the mobile app the user can assign expenses just as I\'d expect any expense app to work, by assigning them to a category (\"meals\")  also to the account it was paid from, i.e. a company credit card or by the employee etc.',
            'context'),
        (
            'In the browser I see no way to select the account the expense was paid from, and therefore no way for the approver to know how the transaction was even paid for.',
            'problem'),
        ('Or for that matter for Xero to know where to assign the transaction?',
         'problem'),
        ('What am I missing??',
         'question'),
        ('Thanks',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 128850,
    'sentences': (
        (
            'I can\'t find a way to nominate an Bank account as closed (so no new transactions) but keep it in the system until the end of financial year.',
            'problem'),
        ('Has anyone done this??',
         'question'),
        ('regards Ian',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 134767,
    'sentences': (
        ('I have a new situation.',
         'context'),
        (
            'A contractor who I normally pay had an invoice owing to me (she pays a base rent when doesn\'t bring in any income).',
            'context'),
        (
            'She had not paid by the time her next \"payment\" from me was made so I deducted the \"monies owing\" (invoice amount) from the bill amount I paid her.',
            'context'),
        (
            'This means that I now have 2 items to deal with:1.  the original invoice she owed eg. $500 looks like its still owing2.  the payment I made to her looks like a part payment of a bill -ie I created the bill as usual for her consulting fees -then deducted what she owed me.',
            'problem'),
        ('So bill $2000 -I paid her $1500.',
         'context'),
        ('Any ideas on how to rectify?',
         'question')
    )
})
questions_sentences.append({
    'question_id': 136639,
    'sentences': (
        (
            'I am working with a client who originally set up their company file in September and added some transactions to the end of the year but did not really start using Xero until January 1, 2012.',
            'context'),
        ('If I change the conversion date to 12/31/11 what happens to the prior transactions?',
         'question'),
        ('Does Xero ignore them?',
         'question'),
        ('Do we need to void them?',
         'question'),
        ('Just trying to figure out the most efficient way to do this.',
         'context')
    )
})
questions_sentences.append({
    'question_id': 138800,
    'sentences': (
        ('If you are a user of Xero and Receipt Bank, tell us how you are getting on and your experience so far.',
         'context'),
        ('Any tips?',
         'question'),
        ('Receipt Bank converts those annoying bits of paper � receipts and invoices - into Xero data, check out .',
         'context')
    )
})
questions_sentences.append({
    'question_id': 135170,
    'sentences': (
        ('It would be great if we could copy an existing standard invoice to a new repeating template.',
         'context'),
    )
})
questions_sentences.append({
    'question_id': 138959,
    'sentences': (
        ('Does anyone know of an App that will allow me to raise invoices in a foreign language?',
         'question'),
        (
            'We need to send out invoices in Japanese and would love to be able to do this without a separate task to duplicate the invoice details.',
            'context')
    )
})
questions_sentences.append({
    'question_id': 137358,
    'sentences': (
        (
            'Hi there,I\'ve successfully been doing payroll for a couple of months, but in December I have a strange occurrence.',
            'context'),
        ('I set the payment up automatically in my bank account so it was paid over the holidays.',
         'context'),
        ('I then reconciled when it came through into Xero.',
         'context'),
        ('But now in my payroll report it shows a deficit for December with the value in brackets.',
         'problem'),
        ('Does anyone have any thoughts on why this might be?',
         'question'),
        ('I thought it might be a coding issue but that seems to be fine.',
         'context'),
        ('The bank account statements match correctly.',
         'context'),
        ('Any help would be greatly appreciated!',
         'outroduction'),
        ('ThanksAndy',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 138085,
    'sentences': (
        (
            'Hi teamCan you please advise whether we need to:> Do a monthly accrual journal for the employer kiwisaver contribution (say 3%) on top of the monthly holiday pay accrual journal',
            'question'),
        ('Many thanksBharat',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 128401,
    'sentences': (
        ('I\'m doing a work around for expense claims.',
         'context'),
        ('I want to import a bill that is on a csv file.',
         'context'),
        (
            'It has several receipts, some of which have different tax rates and all of which will be in different accounts.',
            'context'),
        ('It\'s not clear how to do this when you import a bill using a csv file.',
         'problem'),
        ('Thanks',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 125442,
    'sentences': (
        ('Hi all,I\'m in Canada, and my business is able to file GST using the \"quick method\".',
         'context'),
        (
            'In short, this method is designed to reduce administrative work for small businesses and allows them to pay GST calculated using an approximation of tax owed, based on sales, rather than based on the actual amount collected/paid.',
            'context'),
        (
            'So, for example, I have a sales tax account that says I owe the government $1,000 but the quick method means I only actually owe them $900.',
            'context'),
        ('How can I make an adjustment to my accounts to show that my sales tax owing has reduced by $100?',
         'question'),
        (
            'I tried to do a manual journal, but that doesn\'t work as a manual journal must have equal credits and debits.',
            'context'),
        ('Thanks,-Peter',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 127243,
    'sentences': (
        ('We have a client who uses Farmlands pre the merger of the the 2 firms.',
         'context'),
        ('Can we set up in Xero Using the CRT Co-Op bank feeds form',
         'question')
    )
})
questions_sentences.append({
    'question_id': 133500,
    'sentences': (
        (
            'When sending out payslips to clients, is it possible to add a second email address (CC\'d) that is copied in on each email, we have had a few instances where we have sent Payslips to our clients from Xero and they have confirmed none receipt?',
            'question'),
        (
            'If we can\'t add the option of a cc\'d email address, is it possible to utilise a function that is available for invoices when completed - status is shown as sent and then viewed?',
            'question')
    )
})
questions_sentences.append({
    'question_id': 128766,
    'sentences': (
        ('Hi,We are a high volume store that processes over a hundred transactions per day.',
         'context'),
        (
            'The amount that are paid via EFTPOS show up in the bank as a single transaction (one for each EFTPOS machine).',
            'context'),
        ('Obviously, banked cash shows up as a single deposit.',
         'context'),
        (
            'The problem is, I want to be able to enter sales separated by department of the store, as our expenses are recorded.',
            'problem'),
        (
            'The way we did this with Reckon was an EFT Clearing account, and an Undeposited Funds account, which we then entered a manual journal weekly that credited Sales accounts and debited these two clearing accounts.',
            'context'),
        ('When the money hit the bank, this was credited as coming from these clearing accounts.',
         'context'),
        (
            'I was wondering if there was a better way of doing this in Xero, as it is a lot of manual data entry every week for every store!',
            'question'),
        ('Thanks for your input!',
         'outroduction'),
        ('Jonathon.',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 127873,
    'sentences': (
        (
            'I know that this has likely been asked elsewhere, but I am curious to know whether or not sales invoices and purchase invoices can be partly auto-filled based on previous entries?',
            'question'),
        ('And, if this is possible, can this feature be switched on and off.',
         'question'),
        ('Thanks',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 125842,
    'sentences': (
        ('Why not have as a standard tax code \'Purchases for private use or not income tax deductible\'?',
         'question'),
        (
            'This would allow \'entertainment expenses\' and \'motor vehicle private use\' for example to be set to this tax code thereby automatically populating G15.',
            'context'),
        ('Also note the word \'deductible\' is currently spelt incorrectly on Xero\'s GST Calc W\'sheet!',
         'context')
    )
})
questions_sentences.append({
    'question_id': 138792,
    'sentences': (
        ('If you are a user of Xero and Tanda, tell us how you are getting on and your experience so far.',
         'context'),
        ('Any tips?',
         'question'),
        ('Pay staff correctly for the time they work.',
         'context'),
        ('Manage rostering, time clock attendance & award interpretation with Xero payroll.',
         'context'),
        ('Get the most from your workforce.',
         'context'),
        ('For more information, check out .',
         'context')
    )
})
questions_sentences.append({
    'question_id': 128408,
    'sentences': (
        ('Hi allJust wondering how I would generate a report for sales that lists the marketing link we have put in?',
         'question'),
        ('Eg I want to see what Marketing Produced ho much sales.',
         'context'),
        ('I have already been entering the Marketing option in all invoices.',
         'context'),
        ('Thanks in advance for you help.',
         'outroduction'),
        ('Hope',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 126708,
    'sentences': (
        ('I\'m just getting started with Xero and have a few questions.',
         'context'),
        ('I converted my books from Quickbooks.',
         'context'),
        ('#1 - How is the statement balance calculated in Xero?',
         'question'),
        (
            'My Xero balance is spot on with my bank account, but the statement balance is some number that has never been a statement ending balance or a daily balance in my checking account.',
            'problem'),
        ('I tried following the steps if the two balances don\'t match, but nothing has worked. ',
         'context'),
        ('I figure if I understand how it comes up with it I may be able to tweak some things.',
         'context'),
        ('#2 - Reconciliation seems to encompass much more than I\'m used to.',
         'context'),
        (
            'To me a reconciliation is when you match all your entered transactions with an end of month statement to make sure you have entered everything correctly.',
            'context'),
        ('I don\'t see a way to do this in Xero.',
         'problem'),
        ('Xero seems to only reconcile transactions with daily downloads from the bank.',
         'problem'),
        ('Is there a way to reconcile with a bank statement as well?',
         'question')
    )
})
questions_sentences.append({
    'question_id': 138786,
    'sentences': (
        ('If you are a user of Movemybooks, tell us how you are getting on and your experience so far.',
         'context'),
        ('Any tips?',
         'question'),
        (
            'Sage & Quickbooks to Xero data conversions - the quickest and easiest way to get your clients moved to Xero by UK software version specialists, check out .',
            'context')
    )
})
questions_sentences.append({
    'question_id': 133921,
    'sentences': (
        ('Employees listed by surname first not Christian name',
         'problem'),
    )
})
questions_sentences.append({
    'question_id': 136143,
    'sentences': (
        ('It would be useful if the customised dates chosen in Settings were picked up when generating statements.',
         'context'),
        ('At the moment the due date functionality is only active in generating invoices.',
         'problem')
    )
})
questions_sentences.append({
    'question_id': 137635,
    'sentences': (
        ('I am looking for a fast and easy way to pay a 1099 contractor on a monthly basis.',
         'question'),
        (
            'Our company partnered with an artist to create an app and I am looking for a simple way to pay the artist their share of app sales every month.',
            'context'),
        ('It would be really nice if it could be run with the payroll, since I already do that on a monthly basis.',
         'context'),
        ('Thank you',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 138261,
    'sentences': (
        ('If you are a user of Xero and iKentoo, tell us how you are getting on and your experience so far.',
         'context'),
        ('Any tips?',
         'question'),
        (
            'iKentoo is an enterprise iPad based hospitality POS, which links seamlessly to Xero, and is trusted by over 3000 restaurants and bars worldwide.',
            'context'),
        ('For more information, check out .',
         'context')
    )
})
questions_sentences.append({
    'question_id': 138592,
    'sentences': (
        ('If you are a user of Xero and Hubdoc, tell us how you are getting on and your experience so far.',
         'context'),
        ('Any tips?',
         'question'),
        ('Paperwork on auto-pilot.',
         'context'),
        ('Receipts, bills and statements - all in one place - automatically synced to Xero.',
         'context'),
        ('For more information, check out .',
         'context')
    )
})
questions_sentences.append({
    'question_id': 125276,
    'sentences': (
        ('Hi all,I would like to record all outbound payments within Xero.',
         'context'),
        ('I was hoping to record payments in Xero as and when we pay by bacs or card payment over the phone.',
         'context'),
        ('This works fine when we have been invoiced.',
         'context'),
        ('However, we are on proforma invoicing with some of our suppliers.',
         'context'),
        ('In these instances we tend to pay the proforma, await the invoice before processing into Xero.',
         'context'),
        ('We then spend too long allocating payments as there can be a time before the invoice ends up in Xero.',
         'problem'),
        (
            'I envisaged some sort of merging proforma and invoice together but I don\'t really know what is the correct practice with managing these types of transactions.',
            'context'),
        ('Any help would be much appreciated.',
         'outroduction'),
        ('Thanks,Richard',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 125999,
    'sentences': (
        (
            'Bought 100 Widgets at $10 each on credit card 1, created a bill for $1,000Upon inspection, 10 widgets were damaged, and returned to the supplier.',
            'context'),
        ('They issued a refund to a different credit card.',
         'context'),
        (
            'Credit card 1 shows $1000 expense Credit card 2 shows -$100 (\'income\')I discovered a Bill couldn\'t be used for a negative value.',
            'context'),
        (
            'I understand that a credit note can be created, but since the inventory has been reduced already I think applying the credit note might not work?',
            'question'),
        ('Wondering if an invoice for the 10 widgets with a credit note is the answer?',
         'question'),
        ('Or just an invoice?',
         'question'),
        ('Or something else entirely?',
         'question'),
        ('Thanks in advance for any ideas.',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 126919,
    'sentences': (
        ('Hello,Still getting to grips with Xero.',
         'context'),
        (
            'I am doing my my first pay run and the PAYE, Employee NIC and Employer NIC have correctly deducted from the final amount in \'Step 2. Enter Employee Payments\' however, when clicking through to \'Step 3. Review\' they are  as \'Other payments\'.',
            'problem'),
        ('I have tried changing options but have had no success yet.',
         'context'),
        ('I have classed the 3 pay items above as paid to a contact I created called HMRC - is this correct?',
         'question'),
        ('Any help appreciated.',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 138948,
    'sentences': (
        (
            'My business fixes turf machinery like mowers ect. and we carry a lot of stock eg. bearings, belts ect. We need a simple barcoding system that we scan when it arrives and then scans when we\'ve used it and transfers the data to Xero.',
            'context'),
        ('We\'ve tried stuff like Dear and Unlimited and it just doesn\'t work.',
         'problem'),
        ('Open to suggestions.',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 138016,
    'sentences': (
        ('Where can you view the postings of the payroll journal?',
         'question'),
    )
})

questions_sentences.append({
    'question_id': 137349,
    'sentences': (
        ('i have an employee who is over the age limit for super and now suddenly its telling me i have to pay them',
         'problem'),
    )
})
questions_sentences.append({
    'question_id': 125316,
    'sentences': (
        ('I have a new client that has been using Xero for over a year.',
         'context'),
        (
            'He has some old, unmatched bank transactions from a previous year - so irrelevant - and wants them to just go away.',
            'context'),
        ('Could someone please explain how to delete them.',
         'question'),
        ('Thank you',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 136557,
    'sentences': (
        ('Hi I\'m setting this up for the first time today.',
         'context'),
        ('I\'ve chosen my conversion date to be 1/1/13 so I can start the new year off correctly.',
         'context'),
        (
            'Now I\'m confused because I\'m setting up my bank feed and I\'m being asked to choose which transactions to import - all available or starting on a certain date.',
            'problem'),
        ('Is it wrong to import transactions before Jan 1?',
         'question'),
        ('Thanks.',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 137276,
    'sentences': (
        ('One of our employees has accrued excessive leave.',
         'context'),
        (
            'The Accrual issue is sorted but now i need to remove the excess accrued hours from their leave balance but I cannot figure out how to do this.',
            'problem'),
        ('Thanks',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 138841,
    'sentences': (
        (
            'HiLooking for recommendations for a POS system that sends sales to Xero from my clients cash register in his shop.',
            'context'),
        ('My client sells pet foods so has different tax rates and needs to identify these for VAT purposes.',
         'context'),
        ('Currently my client has a POS system that scans the barcode of the goods and feeds these direct to sage.',
         'context'),
        ('Ideal is to have something very similar to this so as not to disrupt their business unnecessarily',
         'context')
    )
})
questions_sentences.append({
    'question_id': 133559,
    'sentences': (
        ('Working in both the UK and Ireland we have staff i both locations.',
         'context'),
        ('The full payroll features for the UK should be extended to included using Xero within Ireland.',
         'problem')
    )
})
questions_sentences.append({
    'question_id': 126417,
    'sentences': (
        ('We have a client who sends a fixed price purchase order which is then used for a quarter.',
         'context'),
        ('Is there a way to track how much of a client\'s PO has been billed through Xero?',
         'question'),
        ('I was looking at the quote feature but not sure how this would fit the bill...',
         'problem')
    )
})
questions_sentences.append({
    'question_id': 126047,
    'sentences': (
        ('I have a private loan, registered under 900 � Loan in the chart of accounts.',
         'context'),
        ('There\'s no interest on the loan.',
         'context'),
        ('Question 1Company capital from loan',
         'context'),
        ('One part of this loan is to pay a third-party to set up the company.',
         'context'),
        ('The other part (let\'s say 50% to keep it simple) is capital to be put into the company.',
         'context'),
        ('Should this be registered in conversion balances under "881 - Owner A Funds Introduced"?',
         'question'),
        ('Question 2Paying back the loan',
         'context'),
        ('I would like to budget a payback of the loan, over X number of months, but I\'m unsure where to put it.',
         'problem'),
        ('I\'m going over the "Overall budget" but I can\'t seem to find any sensible place to budget for the payback.',
         'problem'),
        ('Thank you so much in advance for your kind help!',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 136009,
    'sentences': (
        ('Hi community,I\'m new to Xero (and very much new to accounting as well, oh the joys).',
         'context'),
        ('I have setup my PayPal feed and it has imported all the transaction lines correctly.',
         'context'),
        ('However the transaction lines pull in the gross value which excludes the paypal fees.',
         'problem'),
        ('How do i show that i have had a fee on certain transactions in Xero?',
         'question'),
        ('What i done on my previous system was every month tally up the paypal fees and add an entry of that value.',
         'context'),
        ('What is recommended?',
         'question')
    )
})
questions_sentences.append({
    'question_id': 125493,
    'sentences': (
        (
            'Hi everyoneI appreciate that this basic question might be beyond the scope of the forum, but I\'m trying to inform HMRC of the fact that this is the end of year PAYE submission.',
            'context'),
        (
            'There\'s a KB article on the Xero site which in turn sends me to a YouTube video from the HMRC about ticking a box on a page in the HMRC portal to tell them that the most recent submission was the last of the year, but I can\'t see that anywhere.',
            'problem'),
        (
            'Given that the video is a bit old, am I to assume that Xero will inform HMRC that this PAYE submission is the last of the year?',
            'question'),
        ('I\'m confused as to how that last piece of the puzzle works.',
         'context'),
        ('I\'ve done my PAYE reconciling and worked through the list of check points in the Xero article.',
         'context'),
        ('There\'s only me on the payroll so I can\'t imagine that anything can go too wrong.',
         'context'),
        ('ThanksOlly',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 138890,
    'sentences': (
        ('Good morning,I wanted to give some feedback on one of the connected apps Veeqo.',
         'context'),
        (
            'This is an inventory management company and having investigated all of the apps this one came out the best for price and features.',
            'context'),
        ('Unfortunately Veeqo is massively let down by the lack of customer service and knowledge that the staff have.',
         'problem'),
        ('We have had many issues since we started to use Veeqo and these have been addressed by the staff.',
         'context'),
        (
            'However, it is incredibly time consuming to get a response, impossible to speak to someone by phone, and became evident that although we went through several induction sessions to discuss the workings of our business Veeqo had not understood our requirements.',
            'context'),
        (
            'The planned meetings we had with various members of staff were regularly late commencing and on occasion did not happen at all.',
            'problem'),
        (
            'The response to this was \"These thing happen in business\"Finally when I tried to submit a complaint it proved impossible to speak to a manger and after over a week of constant e-mails from us we finally receive a response that accepts no responsibility and no solution.',
            'context'),
        (
            'I have worked with many Xero connected apps and as a rule they have all been successful, the companies have been helpful and staff incredibly knowledgeable and forthcoming.',
            'context'),
        ('Most importantly I have always been able to get hold of someone if there have been any issues.',
         'context'),
        (
            'We have now moved to a new Inventory control system (slightly more expensive) and have already seen a massive improvement in service.',
            'context'),
        (
            'I am positive as with most things people have had positive experiences with Veeqo however I wanted to provide feedback for anyone else who is looking for an Inventory add on.',
            'context'),
        ('Thanks',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 137507,
    'sentences': (
        ('Hello,As my employees do not know the business\' nor my twelve month plan.',
         'context'),
        (
            'I prefer that a face to face discussion with myself takes place in the future in regards putting in for leave.',
            'context'),
        (
            'Once we have agreed and discussed all the pros and cons then I would like to enter it in to the Leave section.',
            'context'),
        (
            'At the moment It has given them to much control to discuss and organise their lives around each other without knowing any fundamentals of what is expected at those times of the business and without and consultation.',
            'problem'),
        ('Way to much chit chat already about the Easter break.',
         'problem'),
        ('After the fact puts me in an awkward situation, and it was never like that until these portals arrived.',
         'context'),
        ('I would like pop up options for admin that has a block effect in this case.',
         'context'),
        (
            'That says \"Your employer ass per company policy will need to speak to you before holiday/Leave entry times are requested\".',
            'context'),
        ('Thank you Fabian',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 126360,
    'sentences': (
        (
            'In California - and perhaps other states - goods which are purchased for resale are exempt from Sales Tax on that purchase.',
            'context'),
        ('However some vendors charge tax at the time of sale because they aren\'t set up to handle resale customers.',
         'context'),
        (
            'In this case, the sales taxes paid on goods for resale may be used as an offset against sales tax liability (the forwarding of sales taxes collected on goods sold to the taxing authority).',
            'context'),
        (
            'How should I set up Xero so when I pay sales taxes on goods purchased for resale I can see those amounts on my sales tax report and properly deduct them from my sales tax liability?',
            'question')
    )
})
questions_sentences.append({
    'question_id': 128513,
    'sentences': (
        ('We are considering using Xero as a replacement for our existing bespoke system.',
         'context'),
        ('The guidelines suggest Xero is suitable for 200-500 invoice per month.',
         'context'),
        ('Has anybody any experience of posting more invoices and what happens!',
         'question')
    )
})
questions_sentences.append({
    'question_id': 125471,
    'sentences': (
        ('Hi all, I have two basic questions that I was unable to locate in a search:',
         'context'),
        ('1.) When importing goods from overseas, I am reconciling the transaction at this point without GST.',
         'context'),
        ('Do I record this as \'No Tax\' or \'Tax Exclusive\'?',
         'question'),
        (
            '2.) I am paying the GST as the goods arrive into NZ customs thus there is a separate transaction for the GST alone.',
            'context'),
        ('How do I reconcile this?',
         'question'),
        ('Can I reconcile this as the 820 GST Liability?',
         'question'),
        ('Thanks in advance from a small business owner :)',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 127153,
    'sentences': (
        (
            'How do I split or apportion depreciation expense over various teams using the Auto-Depreciate feature in the FAR?',
            'question'),
        ('It seems you can only allocate one team when setting up the asset in the FAR',
         'context')
    )
})
questions_sentences.append({
    'question_id': 128193,
    'sentences': (
        (
            'Xero has not been prompting for any payroll tax because my s-corp has not paid any payroll this year (yet) to its employee (myself self employed).',
            'context'),
        ('I am in state of Virginia, USA.',
         'context'),
        (
            'Do I need to file a form, pay business state and federal income tax on a quarterly/monthly basis for what my corporation has been generating income every month?',
            'question'),
        ('Or will it be due annually when filed if owed?',
         'question')
    )
})
questions_sentences.append({
    'question_id': 136590,
    'sentences': (
        (
            'A client of mine has been using the new discount feature on sales invoices which is a really handy feature, the problem is that the discount does not appear in the standard .docx template.',
            'problem'),
        (
            'We have not modified this template in any way so I would have expected this to show up as a line item somewhere.',
            'context'),
        ('Discounts do show up on the regular (non .docx) branding theme.',
         'context'),
        ('Am I missing something or do Xero need to modify their .docx documents to present discounting?',
         'question'),
        ('Many thanksSean',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 128792,
    'sentences': (
        (
            'I am trying to find a way to separate the invoices and packing slips, so that when I use \"Print PDF\" it prints both, but when I email I can just email the invoice and not the packing slip.',
            'problem'),
        (
            'I am getting some confused customers wondering why they get a copy of the packing slip everytime I email the invoice.',
            'context')
    )
})
questions_sentences.append({
    'question_id': 137363,
    'sentences': (
        (
            'Hi there,We have some staff paid monthly and one staff member in particular has a few leave requests throughout the month.',
            'context'),
        ('Each leave period shows as a separate line on his payslip.',
         'context'),
        (
            'The payslip looks messy with the multiple leave lines with nothing to differentiate them apart from the number of hours taken and even some of those figures are the same.',
            'problem'),
        ('Is there a way to just make it show as one line or to get details of the leave dates added?',
         'question'),
        ('Thanks,Candice',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 137990,
    'sentences': (
        ('Hello everyoneWe have done our payroll on Xero for the first time in April 2015.',
         'context'),
        ('We noticed that the Employment Allowance is not deducted from the PAYE due payable to HMRC automatically.',
         'problem'),
        ('Xero noted that we need to make a journal entry to be able to claim this.',
         'context'),
        ('The relevant boxes have been ticked as required.',
         'context'),
        ('How do we do this and how do we know the exact amount to be deducted.',
         'question'),
        ('Any comments is greatly appreciated.',
         'outroduction'),
        ('Many kind regardsSylet',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 127493,
    'sentences': (
        ('Hi,When renting our office we paid a security deposit.',
         'context'),
        ('How do i record that in Xero so that we get reminded at the end of the lease to collect it.',
         'question'),
        ('We would like to set up a control.',
         'context'),
        ('Best,',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 135426,
    'sentences': (
        (
            'Hi there,We have just migrated over to Xero from Free Agent, and have noticed we have a tonne of sales invoices listed under our \"awaiting payment\" tab, that aren\'t marked as \"sent\".',
            'context'),
        ('However, when I go into the invoice detail it says \"awaiting payment\"',
         'problem'),
        (
            'Can I therefore assume that these HAVE been sent (even though its\' not marked as such) and that I don\'t need to resend these again?',
            'question'),
        ('FYI these mainly seem to relate to recurring invoices.',
         'context'),
        ('I\'ve also checked under \"history and notes\" section, but it\'s not listed here either.',
         'context'),
        ('Any info gratefully received!',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 137883,
    'sentences': (
        (
            'If employees do not have hours in this payrun should I delete the timesheet for them before I process the payrun?',
            'question'),
        (
            'If I leave them intact (I haven\'t input to them), the pay run generates a small payment for them due to tax refund.',
            'problem'),
        ('In Sage, I would have set these to \'On Hold\' this week.',
         'context'),
        ('Thanks',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 136911,
    'sentences': (
        (
            'Hi,Our Employees, like many other companies in Australia, can accrue a maximum of 76 hours personal leave, once they have reached the 76 we should be able to set a ceiling so it accrues no further.',
            'context'),
        (
            'Resetting to 0 annually doesn\'t work as an employee who hasn\'t taken any time off is still entitled to their 76 hours.',
            'problem'),
        (
            'Example: Jim has been working for Company A for 14 months, he hasn\'t had any time off for personal/carers leave, he gets sick and needs 3 days off so his personal leave balance should reflect 53.2 hours and start accruing again at the weekly rate of 1.4615 until it again reaches 76 hours.',
            'context'),
        (
            'Without a ceiling the accrual is not reflective of actual entitlements and we need to manually go back through the last 12 months for an employee and see how many hours they have taken and subtract that from amount accrued in that period and add the balance accrued before that period.',
            'problem'),
        ('Or we need to make a manual adjustment every week for employees who have reached the maximum.',
         'problem'),
        ('It\'s all very messy and could be easily fixed with a settable ceiling.',
         'context')
    )
})
questions_sentences.append({
    'question_id': 134413,
    'sentences': (
        ('Hi,My inventory items don\'t show in bills.',
         'problem'),
        (
            'They show in invoices on the customer side and in the inventory list itself but they\'re not available for use in bills - there\'s nothing there at all.',
            'problem'),
        ('Anyone got any ideas on this one please?',
         'question'),
        ('RegardsDave',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 128373,
    'sentences': (
        (
            'HelloMy client just change from MYOB to XERO but I am a new XERO\'S user, so I am a bit confuse about how to manage some accounts.',
            'context'),
        (
            'My client has 2 businesses and he pays bills from any of the businesses\' accounts, so we are managing it as a inter-companies loans.',
            'context'),
        ('In MYOB we had set up a credit car account for the inter-companies loan.',
         'context'),
        (
            'When the company paid other\'s company bills, we did spend money from the bank account and increase the loan account balance.',
            'context'),
        (
            'When the other company\'s paid an expense of this company then we transfer the money to the credit card and decrease the balance.',
            'context'),
        (
            'When we received a payment in this account that was other company\'s service we did a receive money and decrease the balance.',
            'context'),
        ('We did something similar with ATO Integrated account.',
         'context'),
        (
            'We created a credit card account, then spend money when we need to enter the GST, PYG, interest etc and transfer money when the payments were done.',
            'context'),
        ('I was able to reconciled it with the ATO statements.',
         'context'),
        (
            'Could I work in the same way in XERO or it looks as a messy books if the  credit card accounts are not reconciled (in the Loan case)?',
            'question')
    )
})
questions_sentences.append({
    'question_id': 127746,
    'sentences': (
        ('How best does one offset an equal debtor and creditor balance that is due to/from the same entity?',
         'question'),
        ('I want to sell a fixed asset to an entity at Net Book Value to a connected party.',
         'context'),
        ('Having followed the help section this will raise a sales invoice (@ nil profit) and raise a trade debtor.',
         'context'),
        ('That same party will also bill me separately a management fee for the same amount.',
         'context'),
        ('This means there will be no cash or VAT impact on either party.',
         'context'),
        ('However it does leave me with a Trade Creditor and a Trade Debtor of equal amounts.',
         'problem'),
        ('How best do I offset these to keep my Xero accounts clean?',
         'question'),
        ('As background info - I\'m winding down a company and want to clear out the balance sheet.',
         'context')
    )
})
questions_sentences.append({
    'question_id': 134977,
    'sentences': (
        (
            'https://community.xero.com/business/discussion/37280114/Kinda similar to this chap..I too have only JUST started using Xero ( and this is my first kinda of accounting software as Im VERY new to this.)Ok..',
            'context'),
        (
            'I\'ve done my best to go through as much as possible on the software and Ive jumped on in and attempted to swim along.',
            'context'),
        (
            'However, i THEN found out / noticed I needed to enter in starting balances etc etc to begin with and I basically didnt do this...',
            'context'),
        ('1/ Ive basically done the following.',
         'context'),
        (
            'I\'ve imported my HSBC cvs bank statements from July  1 2014 to Jun 30th - Our Financial Year 2/ I\'ve reconciled the statements with the sales and purchases and naturally a report has been produced...',
            'context'),
        (
            '3/ Everything seemed to me seemed ok on the reports4/ My accountant has access to this now, to make life easier (which is what swung me toward using the software as I like the mobile functionality of which I KNOW i can pass on and teach to my colleagues within the business just to help streamline things on a daily basis and stay completely upto date.',
            'context'),
        (
            '5/ My accountant has informed me of my balances (from my previous accounting year) though I was going on my bank statement itself 6/ So I entered them into \"Conversion Balance\" section but apparently still things are not right?',
            'problem'),
        ('Am I doing something wrong ?',
         'question'),
        (
            'should I start again (id rather not as I\'ve reconciled things in details, even giving descriptions on many itemsalso, my Xero Balanced don\'t seem to match up eitherI hope someone can help me as I really don\'t want to be now going back to excel as this looks like great software.',
            'context'),
        ('Hope this makes sense!!',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 139606,
    'sentences': (
        ('Hi there,What information do I need to work out whether a 3rd party software will link into Xero?',
         'question'),
        (
            'I am look at a lease management software, which as a feature has an accounting link allowing information to be exchanged (especially accounts payable).',
            'context'),
        ('Regards,Patrick',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 138130,
    'sentences': (
        (
            'Trying to post payroll this afternoon, and when I went to approve the timesheets I get the error message\"An error has occured. Your Payslip may be out of sync. Try again in a moment.\"',
            'problem'),
        ('I have been re-trying for an hour now.',
         'context'),
        (
            'I have logged a support request but the response time to that is potentially 24hrs, and I would like to pay the staff today.',
            'context'),
        ('Has anyone come across this error and a potential fix/workaround.',
         'question')
    )
})
questions_sentences.append({
    'question_id': 139038,
    'sentences': (
        (
            'Hello,I am looking for either a business owner or accountant who is familiar with and knows in detail the pro\'s and con\'s of how certain programs work with Xero and can offer advice on a possible solution.',
            'context'),
        ('I am starting a new business in the UK and i want to sell both retail online and wholesale in person.',
         'context'),
        (
            'I have picked Xero as my accounts package, Shopify as my online solution and i am wondering if i can run my business on just that or if i need a inventory app also.',
            'question'),
        (
            'Here are the key issues: I import 100% from overseas with long lead times, so working out costings and creating purchase orders and Invoices months in advance is a question.',
            'context'),
        ('Is Xero a good program as central data file for products?',
         'question'),
        ('Does this info flow to shopify or do i need to duplicate data?',
         'question'),
        ('Are the basic apps for shopify any good for linking to Ebay and Amazon?',
         'question'),
        ('I dont have a warehouse or staff, i plan to contract out all logistics to a 3PL.',
         'context'),
        ('I have been looking at inventory apps such as Deer, Unleashed, Trade Gecko or Cin7.',
         'context'),
        (
            'Cost is a factor but it would be great to talk to someone who has used any of these with Xero and offer advice.',
            'context'),
        ('Many ThanksNathan',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 140003,
    'sentences': (
        ('Right, sick of Xero payroll.',
         'context'),
        ('Can anyone please recommend a payroll add-on that is not too expensive?',
         'question'),
        ('Thank you',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 128480,
    'sentences': (
        (
            'For small business clients, there should be option for calculating depreciation and disposal and addition for pooled assets.',
            'context'),
        (
            'Rules are quite different from normal diminishing value method hence we have to prepare manual work-paper to calculate depreciation and have to post it manually',
            'problem')
    )
})
questions_sentences.append({
    'question_id': 133937,
    'sentences': (
        ('Xero Payroll does not calculate wages based on the employees start date.',
         'problem'),
        (
            'If your employee starts halfway through a pay run/ pay period, a manual adjustment of their hours and tax will need to be done.',
            'problem'),
        ('For example:',
         'context'),
        ('1. We use a monthy pay cycle that ends 28th of each month',
         'context'),
        ('2. We have setup a new employee, set the start date as 5th November 2012',
         'context'),
        ('3. We have setup employee with annual salary, based of 40 hours work week.',
         'context'),
        ('4. When we do a pay run, xero calculates the employee worked 23 days worth of hours, instead of 18.',
         'context'),
        ('It has thus NOT taken into account their start date, but used the entire month.',
         'context'),
        (
            'I can work around the problem by adjusting the number of hours after doing a pay run, but this is clearly undesirable and error prone (especially as wage costs are a large part of our business and getting these wrong is costly)',
            'context')
    )
})
questions_sentences.append({
    'question_id': 127511,
    'sentences': (
        ('Hi I have a case of new fixed asset, where 03 payments were made on different dates to buy the same item.',
         'context'),
        ('01- Downpayment - paid thru Debit Card on 1st of May',
         'context'),
        ('02- 1st partial payment - paid thru Credit Card on 15th of May',
         'context'),
        ('03- Final payment - paid thru EFT on 20th of May',
         'context'),
        ('Under fixed assets these three transactions are appearing as 03 different assets.',
         'problem'),
        ('How do I combine them into 01 Asset.',
         'question'),
        ('Appreciate any reference or solution.',
         'outroduction'),
        ('Regards',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 134704,
    'sentences': (
        ('Hi.',
         'context'),
        (
            'I\'m switching my bank account to The Co-operative Bank UK and I see there\'s a feed available for (Personal Banking) which I need.',
            'context'),
        ('Every time I try to set up the feed, Xero tells me that the access to my online banking is locked.',
         'problem'),
        (
            'On contacting The Co-operative Bank they tell me they have updated their online banking system so that the questions that Xero asks will no longer be acceptable.',
            'context'),
        ('Could you look into this please as I really need to set this feed up as soon as possible?',
         'question'),
        ('It seems the questions you need to ask are different and I do know the answers!',
         'context'),
        ('Many thanks.',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 127502,
    'sentences': (
        (
            'Hey Guys,I recently added some funds into my business account as my cash flow was running low and then within a few weeks, transfered the same amount back to my personal account.',
            'context'),
        ('How do I account for this on Xero as the transaction appear on the  bank feeds.',
         'question'),
        ('Thanks,Ket',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 126366,
    'sentences': (
        ('I used some convenience checks from a credit card to pay some vendors.',
         'context'),
        ('Xero excludes ALL credit card transactions and PayPal transactions.',
         'context'),
        (
            'After some research, it appears as though these transactions do no meet the definition of \"purchase card transaction\" and as such would not be reported by the PSE (Payment Settlement Entity i.e. the credit card company) on a form 1099-K.',
            'context'),
        (
            'Seems like Xero needs to add a check box somewhere that would allow these transactions to flow into the 1099 query report.http://www.marcumllp.com/blog-tax-and-business/new-form-1099-k-filing-requirement-for-merchant-card-and-third-party-network-payments',
            'problem'),
        (
            'This link is about federal agencies, but Q-32 I think still applies and explains it: https://www.irs.gov/Government-Entities/Federal,-State-&-Local-Governments/Federal-Agency-Frequently-Asked-Questions',
            'context'),
        ('Any ideas on a work around until Xero fixes this?',
         'question'),
        ('Or am I wrong?',
         'question')
    )
})
questions_sentences.append({
    'question_id': 126442,
    'sentences': (
        ('Hi there,Lets say I want to record the costs of a meal with a potential client.',
         'context'),
        ('How would I go about it?',
         'question'),
        ('With the flat chart of accounts, I cant create a food sub account to the biz Dev account.',
         'context'),
        ('Is this when tracker would come in handy?',
         'question'),
        ('Thanks,Duncan',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 136815,
    'sentences': (
        (
            'Hi I have only been using xero for a few months and have just noticed that on our profit an loss statement the wages figures are showing up twice once as a net figure and once as a gross figure and therefore throwing out our monthly figures',
            'problem'),
        ('Am I reconciling the wages wrong or how do i fix this?',
         'question'),
        ('Meaghan',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 126837,
    'sentences': (
        ('I am coming from Quickbooks and I am setting up my chart of accounts.',
         'context'),
        ('I am not familiar with setting a tax rate for each account.',
         'context'),
        ('For example, I have a computer sales account I need to add to record our computer sales in.',
         'context'),
        (
            'With Quickbooks I  normally would just set sales tax (7%) per invoice or per item I was selling and the item would be tied to the correct sales account.',
            'context'),
        (
            'Do I need to set a tax rate on the actual account if I set tax rate for the item or can I just leave it at zero?',
            'question')
    )
})
questions_sentences.append({
    'question_id': 136854,
    'sentences': (
        ('I have a problem with the super setup.',
         'context'),
        ('It is the first time I try to set this up.',
         'context'),
        ('I have signed up with ClickSuper.',
         'context'),
        ('Question 1.',
         'context'),
        ('Now under my Settings -> Superannuation, I got 2 super funds that I added in.',
         'context'),
        ('Namely ANZ and HOSTPLUS.',
         'context'),
        (
            'I want to use HOSTPLUS as default and only super fund, and remove the ANZ one, but the ANZ line has a little LOCK icon there and I cannot delete it.',
            'problem'),
        ('Question 2.',
         'context'),
        ('Does Xero/ClickSuper automatically draw funds from my bank account to pay the funds for me?',
         'question'),
        ('If Not Should I go to HOSTPLUS to do this manually?',
         'question'),
        ('Question 3.',
         'context'),
        (
            'Some of the guys in company are long-term contractors, so they are not in �Employees� list in Xero, in this case, how do I handle super for them in the system?',
            'question'),
        ('Looking forward to your answers and thanks very much.',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 133954,
    'sentences': (
        (
            'When a supplier requires a deposit up front with the balance to be paid on delivery, how can duplicate fixed assets in Xero be avoided?',
            'question'),
        ('We recently ordered custom computer equipment and paid a deposit upon ordering.',
         'context'),
        ('This transaction created a new fixed asset in Xero that I have since registered.',
         'context'),
        ('We\'ve now paid the balance owing and this 2nd transaction has created a duplicate fixed asset record.',
         'context'),
        (
            'I will probably delete the new fixed asset but would like to be able to have both the deposit and balance payment transactions linked to the asset record.',
            'context'),
        ('Is this possible in Xero?',
         'question')
    )
})
questions_sentences.append({
    'question_id': 139941,
    'sentences': (
        (
            'We have set our default to be Tax Inclusive on our sales invoices but see when we start a new invoice it reverts to Tax Exclusive.',
            'problem'),
        (
            'Do you have a fix for this as I can\'t see anything that we could be doing wrong here, as when I go back to check the setting it Tax Inclusive is definitely selected and saved.',
            'question'),
        ('Thanks',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 135033,
    'sentences': (
        (
            'Hi There,I\'m currently researching new accounting platforms for my company and wanted to check in with you Xero users as to the feasibility of Xero for our use case.',
            'context'),
        (
            'The company I work for is a manufacturing company with about 75 employees (about 25 office staff and 50 factory workers).',
            'context'),
        (
            'Our revenue is about $10 million per year, but our accounting practice isn\'t very different from a small business.',
            'context'),
        ('PO\'s from customers, send invoices, pay bills.',
         'context'),
        ('Nothing too crazy.',
         'context'),
        ('My main concern is with transaction limits and scalability.',
         'context'),
        (
            'We process about 460 invoices per month across about 140 customers (total customers in our database are about 500 to 600).We sell about 200pcs per month across 850 sku\'s.',
            'context'),
        ('We process about 110 checks per month to 40 vendors or so.',
         'context'),
        ('I\'m going to follow up with Sales/Support, but I wanted see if I could get some input from actual users.',
         'question'),
        ('Thanks for any info you can provide!',
         'outroduction'),
        ('-Bradley',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 138770,
    'sentences': (
        ('If you are a user of Xero and invitbox, tell us how you are getting on and your experience so far.',
         'context'),
        ('Any tips?',
         'question'),
        (
            'Automated line-by-line data extraction from accounts payable bills - seamlessly sent to Xero, inventory systems and a cloud-based filing cabinet, check out .',
            'context')
    )
})
questions_sentences.append({
    'question_id': 127386,
    'sentences': (
        ('Is it possible to get year to date balance on the payslip like what appears in MYOB.',
         'question'),
    )
})
questions_sentences.append({
    'question_id': 127934,
    'sentences': (
        (
            'Hi there, A customer has paid twice so I am wanting to allocate his payment as a credit to him, there is no invoice to allocate it to.',
            'context'),
        ('What is the best way of allocating this?',
         'question'),
        ('Thanks, Jo',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 125408,
    'sentences': (
        ('I understand what tracking is.',
         'context'),
        ('I have a company that has several locations.',
         'context'),
        (
            'Can I export all my accounts put a track on them and then import them back into Xero or should I just wait till 01/07/17 and start from there.',
            'question')
    )
})
questions_sentences.append({
    'question_id': 135963,
    'sentences': (
        ('Could you please put the name of the contact on statements.',
         'question'),
        ('Right now it has company and address only.',
         'problem'),
        ('I would like to see the contacts name.',
         'context'),
        ('Thank you',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 126642,
    'sentences': (
        (
            'Is it just me being a Xero novice or is there a way to show a VAT summary table consisting of TaxCode, NetGoodsAmount and TaxTotal on a custom invoice using just the default currency.',
            'question'),
        (
            'It seems that Xero will do exactly what I want using the Currency Conversion table but only when the invoice is in a foreign currency.',
            'context'),
        ('I would like to have a very similar table on invoices using just the default currency.',
         'context'),
        ('Is this the Achilles heel of Xero?',
         'question'),
        (
            'In my previous accounting package (that will remain nameless) I had a VAT summary table on all my invoices (It was impossible to get rid of it!).',
            'context'),
        (
            'Nearly every invoice I look at from my suppliers shows the VAT rate, the net total amount it applies to and the corresponding tax total in a table.',
            'context'),
        ('So what am I doing wrong that means all I can show in Xero is the Tax Code and its Tax Total?',
         'question'),
        (
            'I know legally it might not be essential but it\'s almost a courtesy to whomever has to handle the paperwork.',
            'context'),
        ('I have asked Xero support but as yet had no reply.',
         'context'),
        ('Is there anyone in the Xero community that can put me straight, please?',
         'question'),
        (
            'I\'ve been on this for three days solid and although I now have improved greatly my understanding of Word am no closer to achieving the invoice template I would like.',
            'question'),
        ('Any assistance will be greatly appreciated.',
         'outroduction'),
        ('Thank you in advance for your time!',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 127673,
    'sentences': (
        ('Hi ThereJust wondering if there\'s a functionality to access an employees prior year Payment summary?',
         'question'),
        ('For example right now when I click into an employee I can only access their 2013 PAYG PS.',
         'context'),
        ('Thanks in advance for your help.',
         'outroduction'),
        ('Amelia',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 135252,
    'sentences': (
        (
            'For bank accounts that are not connected to a bank feed, it would be nice to be able to go to the account transaction page and select each transaction and like you do with remove & redo, have a reconcile option.',
            'problem'),
        ('This eliminates the need to go into each transaction manually to reconcile.',
         'context')
    )
})
questions_sentences.append({
    'question_id': 136174,
    'sentences': (
        (
            'Change \'amounts are in...\' to \'no tax\', and then then either \'tax inclusive\', or \'tax exclusive\' -- VAT doesn\'t get updated any more.',
            'problem'),
        ('Marcin',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 138033,
    'sentences': (
        (
            'Hi,I ran our first pay run last Friday and although we have claimed the Employment Allowance, the charge we would have incurred is showing on the P&L.',
            'problem'),
        (
            'It has definitely worked and on the RTI details, it shows the charge being deducted via the EA, however the charge is there....',
            'context'),
        ('Am I losing my mind?',
         'question'),
        ('Thanks in advance,Caroline',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 134960,
    'sentences': (
        ('Hi there,I\'m still learning xero and accounting so bear with me!',
         'context'),
        (
            'Through this tax year we\'ve accidentally been using owner funds introduced + owner drawings + directors loan account to record personal money in and out.',
            'context'),
        (
            'We\'re a ltd company, so I want to use just the director\'s loan account and therefore need to consolidate owners funds introduced and owner drawings into the DLA.',
            'context'),
        (
            'I suppose I could go into each of the transactions (mostly expense claims) undo the payments and recode them to the DLA, but this would take some time and every adjustment (i would assume) will appear on our latest VAT return.',
            'problem'),
        ('Is it possible / advised to just make lump sum transfers from the 2 owners accounts into the DLA?',
         'question'),
        (
            'This would tidy everything up, but i\'m not sure how i would do this and whether there are any disadvantages to doing so',
            'problem'),
        ('Many thanks!',
         'outroduction'),
        ('Hazel',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 126374,
    'sentences': (
        (
            'I have a large fixed asset register, and 9 months into the tax year it is not feasible to rollback depreciation to the beginning of the year just so that I can dispose of an asset without incurring depreciation in the current year.',
            'problem'),
        (
            'There have been other disposals and journals created during the course of the year, and repeating the disposal of these assets is not an option.',
            'context'),
        ('This was not a problem prior to the November 2015 improvements.',
         'context'),
        (
            'I have endeavoured to set a zero depreciation rate, which the system will not accept, and also to reset the asset to having no depreciation, which the system will not allow me to do.',
            'problem'),
        ('I am inclined to think that a fix needs to be created.',
         'context'),
        ('Does anyone have a solution.',
         'question')
    )
})
questions_sentences.append({
    'question_id': 127270,
    'sentences': (
        ('I\'ve purchased some whitegoods on a store credit card and I\'m not sure how to manage the payments.',
         'context'),
        ('When I do a bpay to my card, what do I code the payment as?',
         'question'),
        ('The help file recommends to code it as an equity account (such as owner funds introduced).',
         'context'),
        ('If I do that, how to I account for the assets?',
         'question'),
        ('Thanks for any assistance.',
         'outroduction'),
        ('Matt.',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 138000,
    'sentences': (
        ('Hi, new to payroll,Have completed my first run and have posted it.',
         'context'),
        (
            'I can\'t now understand if I have to pay the employees from my business bank account or what I have done has generated a payment to them.',
            'context'),
        ('It seem unclear.',
         'problem'),
        (
            'When I look on line it talks about clicking on employee batch payment tab to generate a payment but I do not have that anywhere so left feeling very confused.',
            'context'),
        ('Pay is due tomorrow, do I pay manually or not?',
         'question'),
        ('Prompt help would be appreciated.',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 126368,
    'sentences': (
        ('Hi, My client runs a business in the clothing industry supplying clothing to schools, clubs and businesses.',
         'context'),
        (
            'I have set up 2 tracking categories, Size and Colour,  to allow him to use these specifically for invoicing customers.',
            'context'),
        ('This is a great feature as he can make an appropriate selection on screen while invoicing.',
         'context'),
        ('My client wants the tracking category of Size and Colour to appear the invoice to his customers.',
         'context'),
        (
            'It would appear the tracking category field names are not available to customise the invoice or, I just haven\'t found them.',
            'problem'),
        (
            'Can you please provide some feedback about the tracking category field and whether I can incorporate same in to customising invoice?',
            'question'),
        ('My client will not be using tracking categories for reporting purposes, only to invoice.',
         'context'),
        (
            'Should the feature not be available to include in customising invoices, then how soon before this can be available?',
            'question'),
        ('Thank you & regards, Robert',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 128558,
    'sentences': (
        ('HI , how do i input opening balances for my customers without importing them ?',
         'question'),
    )
})
questions_sentences.append({
    'question_id': 125477,
    'sentences': (
        ('I cannot find how to achieve this so hope someone can help...',
         'problem'),
        (
            'Multiple payments (2) were made to a supplier for a number of products (3) received, because a \'difference\' payment had to be made a few days later (but before I was invoiced) to account for a change to a superior product.',
            'context'),
        (
            'These 2 payments are showing up as separate lines in my company credit card account ready for reconciliation.',
            'context'),
        (
            'Using the three separate invoices (that correctly show the 3 products I received) from the supplier I created a transaction (made up of the 3 items) which totalled the same \'spent\' value as the 2 credit card account statement lines, however there is no option to \'split\' this transaction like there is with invoice payments that I can see?!',
            'problem'),
        (
            'Therefore when I choose \'match\' against either of the statement lines, I can see the transaction, but cannot proceed.',
            'problem'),
        (
            'Please advise if this requires the implementation of additional functionality or if I should undertake this reconciliation using a different process?',
            'question'),
        ('Many Thanks / Dan',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 136360,
    'sentences': (
        (
            'Hi,We are evaluating new accounting systems and I have a requirement that does not seem to be available in entry level/mid-market systems.',
            'context'),
        ('1. Budgets and actuals',
         'context'),
        ('2. Time sheets',
         'context'),
        (
            '3. Travel and expense reportingWe need budgets and actual cost tracking for a software company, (what Oracle would call Projects)For example let\'s say that we have  the following items  100:  Software Module 1 (project 1_120:  Feature x (project 2)200:  Project 3etc.',
            'context'),
        (
            'Let\'s say we have 25 developersLoaded costs could vary for each let\'s say $120 to $300 per hourThe managers define a project and let\'s say they budget $50,000 for a project (e.g. Project 31)We\'d like the team to enter their time and associate it with a budget item number (100, 120, 200) etc.',
            'context'),
        ('I\'d like to know how much we are spending on each project and how well are we planning/executing.',
         'context'),
        ('We want to go to a cloud based system.',
         'context'),
        ('Thanks',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 137257,
    'sentences': (
        (
            'Hi there, I have a staff member employed as a casual that is not entitled to superannuation payments (I have checked the award legislation), but Xero won\'t let me process her pay runs without adding a super line.',
            'problem'),
        ('Also, even though she is registered as a casual under \'taxes\' it still requires a super line.',
         'problem'),
        ('Are there settings to eliminate this line so that I can still process pays?',
         'question'),
        ('Much appreciated!',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 126071,
    'sentences': (
        ('Morning,I need some advice on how to correctly input vehicle registrations.',
         'context'),
        ('I have just noticed that I have inputted my vehicle registration details incorrectly.',
         'context'),
        (
            'EG 6 months rego is $451.60so xero is calculating the GST of $41.05However the GST component is only calculated on Insurance so the correct amount of GST is $17.32',
            'context'),
        ('Advice is greatly appreciated thank you',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 125619,
    'sentences': (
        ('Hi,I am new to Xero and accounting in general.',
         'context'),
        ('I have started a used car sales business (in Scotland, UK).',
         'context'),
        ('When buying a car to fix up and sell, is this a direct expense or should it be put in cost of goods sold?',
         'question'),
        (
            'Also and repair costs, MOT, bodywork and work outsourced (paintwork, mechanics etc) for said car is this a direct expense or a cost of goods sold?',
            'question'),
        (
            'Finally, each car is advertised individually, as its part of the cost of selling said car is this a direct expense of cost of goods sold?',
            'question'),
        ('Or should it be put in the advertising account?',
         'question'),
        ('Any help would be gratefully receivedMany thanksEric',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 138930,
    'sentences': (
        ('I\'m looking for a time tracking tool (mainly to use for consulting work) that works well with Xero.',
         'context'),
        ('Has anyone used either Work Flow Max or Harvest?',
         'question'),
    )
})
questions_sentences.append({
    'question_id': 135709,
    'sentences': (
        ('I have one organisation in Xero, which gives three partners (and our accountant) different levels of access.',
         'context'),
        ('I have been asked to take on another organisation, with different partners but the same Accountant.',
         'context'),
        (
            'I know I can add another organisation to Xero (saving money in doing so) and restrict user access o different activity levels within that organisation.',
            'context'),
        (
            'However, can I restrict each business\'s user access, so that users from \"Business A\" cannot view \"Company B\"s affairs (and vice versa), while the accountant and I can access both, via two log-ins or whatever?',
            'question'),
        (
            'Apologies if this has already been answered, I did look and checked the closed thread, but couldn\'t find what I was looking for in existing threads.',
            'context'),
        ('If one already exists, please link me to directly, it so I don\'t waste anyone\'s time.',
         'context'),
        ('Many thanksAdrian',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 136403,
    'sentences': (
        ('I am relatively new to Xero and running a small business.',
         'context'),
        ('I set up my Sales Invoice but It took a few weeks to set up my Bank Account.',
         'context'),
        ('I now have a bank account and entered the details into Xero.',
         'context'),
        ('I want the details to automatically appear on my Invoices so people can pay me by direct transfer.',
         'context'),
        (
            'I have tried to work it out via the Sales Invoice settings but it seems you can do everything other than check a tick box to display the bank details.',
            'problem'),
        ('How do i do it?',
         'question')
    )
})
questions_sentences.append({
    'question_id': 128431,
    'sentences': (
        ('My business allows patients to pre-purchase rehab consultations in bulk, at a discount.',
         'context'),
        ('We invoice for each of the treatment sessions, and then allocate the invoice to the pre payment.',
         'context'),
        (
            'But I would like to run a report that shows me all of the prepayments currently outstanding for all patients.',
            'context'),
        (
            'The only way I can see at the moment, is to run the Aged Payables report, and check each invoice individually.',
            'problem'),
        ('I\'m sure there must be a better way?',
         'context'),
        ('Can I filter the Aged Payables somehow to show me just the unallocated Prepayments?',
         'question')
    )
})
questions_sentences.append({
    'question_id': 138808,
    'sentences': (
        ('If you are a user of Xero and simPRO, tell us how you are getting on and your experience so far. Any tips?',
         'question'),
        (
            'Your comprehensive software tool for Electrical, Plumbing, Security, Heat Pump, HVAC, Service & Blue Collar Industrial Contracting Businesses: 1-100 staff, check out .',
            'context')
    )
})
questions_sentences.append({
    'question_id': 139273,
    'sentences': (
        ('Can anyone recommend a good point of sale system for a Bar/Restaurant that integrates with Xero?',
         'question'),
        (
            'We have implemented Vend for retail clients but it is missing some functionality needed for a restaurant such as table layouts.',
            'context'),
        ('Vend themselves even state that it is not really suitable for a bar/restaurant.',
         'context'),
        (
            'I have been trying Epos Now which looks good but they are based in the UK and I am concerned at their very sparse documentation on how to use the system.',
            'context'),
        (
            'Any advice or examples of what bars and restaurants that use Xero are using for their POS would be greatly appreciated.',
            'context'),
        ('regards,Brendan',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 138528,
    'sentences': (
        (
            'If you are a user of Xero and MyDesktop, tell us how you are getting on and your experience so far. Any tips?',
            'question'),
        (
            'The industry leading web-based sales, listing and CRM technology that helps you run a successful real estate agency.',
            'context'),
        ('For more information, check out .',
         'context')
    )
})
questions_sentences.append({
    'question_id': 128337,
    'sentences': (
        (
            'Ive had a search for this and there are three treads which seem to discuss a similar thing, however each are missing one key fact.',
            'context'),
        ('Firstly the background.',
         'context'),
        ('We use Workflow Max to generate an invoice and that automatically gets fed into Xero as a draft.',
         'context'),
        ('All ok from here.',
         'context'),
        (
            'Then we adjust in Xero where appropriate if needed and then send the invoice as an email WITHIN Xero using the following options selected (not sure if that has anything to so with this issue, but giving the full workflow):Include files as attachments YESInclude PDF attachment YESSend me a copy (accounts@***.co.uk) YESThis goes off to the client and I receive my copy into my outlook inbox, so the invoice has definitely been sent.',
            'context'),
        ('HOWEVER, and this is where it gets odd.',
         'context'),
        (
            'When I look down my list of invoices sent out in the \"Invoices Awaiting Payment\" page it clearly shows that the most recent invoices not as being sent, I.E. the word \"Sent\" in green is not showing besides it in the list.',
            'problem'),
        (
            'If I select the invoice and select it\'s history it clearly shows three things (for example):Created17 Nov 2015 11:07 a.m. System GeneratedReceived through the Xero API from WorkflowMax Invoice sent 17 Nov 2015 11:30 a.m. Shake AccountsThis invoice has been sent to David@***.co.ukApproved17 Nov 2015 11:31 a.m. Shake Accounts INV6212 to **** Ltd for &#163;99.99.',
            'context'),
        (
            'So everything is showing that it appeared in Xero from Workflow Max, was sent via email within Xero and then was approved by me.',
            'context'),
        (
            'Surely if it goes through the process of sending the invoice, it should mark it as sent as everything apart from the initial import is done within Xero.',
            'problem'),
        ('(We do generate invoices directly within Xero too and we get the same issue).',
         'context'),
        (
            'I must stress, this never affects clients paying, they always receive the invoices, so that is not the issue, the problem is the invoices are simply not showing as sent in searches.',
            'context'),
        ('Any help greatly appreciated.',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 128814,
    'sentences': (
        ('New to Xero.',
         'context'),
        ('Trying to setup basic COGS accounts in the chart of accounts - ie. Opening Stock, Purchases, Closing Stock.',
         'context'),
        (
            'Just wish to code all purchases to Purchases, and do a simple journal monthly to record current stocks and produce P&L report with gross profit showing.',
            'context'),
        ('Cannot see how to do this in Xero.',
         'problem'),
        ('It is simple in MYOB chart of accounts.',
         'context'),
        ('I\'ve googled all day and cannot find an answer.',
         'context'),
        ('Can anyone help please?',
         'question')
    )
})
questions_sentences.append({
    'question_id': 135373,
    'sentences': (
        (
            'Hey, I\'d love some help, when I click on the green arrow to repeat the amount I have added in Budget Manager, it changes what it does each time.',
            'problem'),
        (
            'Sometimes it works, however most of the time, it deletes the amount I have put in and starts with the amount I\'ve told it to increase by?',
            'problem'),
        ('Amy thoughts would be appreciated.',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 138571,
    'sentences': (
        (
            'If you are a user of Xero and Constant Contact, tell us how you are getting on and your experience so far. Any tips?',
            'question'),
        (
            'Easily create beautiful emails and reach your customers where they are every day: their inbox. Export lists from Xero to Constant Contact.',
            'context'),
        ('For more information, check out .',
         'context')
    )
})
questions_sentences.append({
    'question_id': 139344,
    'sentences': (
        (
            'I currently use Harvest for all my invoicing and link it with Xero to reconcile transactions and prepare BAS.',
            'context'),
        (
            'I have noticed on Harvest that when I set up a new invoice it has the following message \"Apply Tax From Xero\".',
            'context'),
        (
            'After starting to put the BAS together today, it looks like Xero is saying that these invoices are BAS excluded.',
            'problem'),
        ('How do I change this?',
         'question'),
        ('I can\'t seem to find settings in either Xero or Harvest.',
         'problem'),
        (
            'It affects reconciliation when Xero picks up a related payment from Harvest (Match) rather than when I create (and can ensure it is included in BAS)',
            'context'),
        ('Many thanks',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 139841,
    'sentences': (
        ('Hi XeroI have two Xero accounts for different entities, Global Search works for one but not the other.',
         'problem'),
        ('Support have identified the problem for some users and I would like to know when it will be fixed.',
         'question'),
        ('It has been over a month now.',
         'context'),
        ('Thanks',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 126322,
    'sentences': (
        ('I am wondering if anybody here has good suggestions on software we can use for tax returns.',
         'question'),
        (
            'I was hoping to use Turbotax because it has great review and looks complete and very user friendly but apparently, it only integrates with Quickbooks.',
            'context'),
        ('Any suggestions?',
         'question')
    )
})
questions_sentences.append({
    'question_id': 128199,
    'sentences': (
        ('Hi! I am currently customising a docx invoice template.',
         'context'),
        (
            'I would like the invoice to display two extra lines showing \"Invoice Total\" and \"Less Payments Received\" if payment has already been made prior to generating the invoice.',
            'context'),
        ('Or if payment has not been made, I would like it to just display the invoice total.',
         'context'),
        ('I have gotten this far with the first extra line using the following IF function:',
         'context'),
        (
            'questions_sentences.append({ IF &#171;StatementType&#187; > 0 \"Invoice Total\" \"\" backslash* MERGEFORMAT })questions_sentences.append({ IF questions_sentences.append({ MERGEFIELD InvoiceTotalNetPayments backslash* MERGEFORMAT }) > 0 questions_sentences.append({ MERGEFIELD  InvoiceTotal backslash# \"#,##0.00;(#,##0.00)\" backslash* MERGEFORMAT }) backslash* MERGEFORMAT })',
            'code'),
        (
            '(Note: I\'ve used the actual backslash symbol - not just written backslash! - however I was not able to type that symbol in this post...)',
            'context'),
        (
            'The \"Invoice Total\" label seems to display correctly according to whether or not payment has been made (first IF function), but the amount of the invoice (second IF function) displays this error message:Error! Unknown op code for conditional.',
            'problem'),
        ('> 0 and then the invoice amount shows correctly.',
         'context'),
        ('Can anyone help?',
         'question'),
        ('I feel like I just have a small typo that is preventing me from getting the correct formula.',
         'context'),
        ('I\'ve spent a long time searching help but no luck.',
         'context'),
        ('Thanks in advance!',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 134637,
    'sentences': (
        ('Hi there,I was wondering if anyone can help.',
         'context'),
        (
            'I have allocated 2 credit notes to one invoice for one of our clients and I\'d like to keep those credit notes as 2 separate lines with corresponding amounts when I print the invoice as PDF.',
            'context'),
        ('At the moment Xero creates one line, a sum, out of those two credit notes.',
         'problem'),
        ('Many thanks,Nicholas',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 135510,
    'sentences': (
        ('Hi I am new to xero, I am having trouble when raising invoices.',
         'context'),
        ('When I raise the invoice and save it is not automatically emailing my customer.',
         'problem'),
        ('I am having to then go back into the invoice to manually send the invoice.',
         'problem'),
        ('I am worried that the reoccuring invoices may not send in the future.',
         'context'),
        ('Thank youChris',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 126239,
    'sentences': (
        ('I shared a networking lunch with other business owners and we spilt the bill.',
         'context'),
        ('I paid cash for my part and only have a copy of the invoice for the entire group.',
         'context'),
        (
            'I can reconcile my part payment against the invoice then am left with an outstanding amount still showed as owing.',
            'context'),
        ('however that amount was paid by the other people.',
         'context'),
        ('How do i remove this amount from Xero?',
         'question'),
        ('Should i edit the invoice amount OR use some form of credit note?',
         'question'),
        ('However, if I do the latter then it will still show up in my accounting records',
         'problem'),
        ('Angus',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 125593,
    'sentences': (
        (
            'Hi everyone, When I process a batch payment, the details field automatically updates to a default detail from a previous payment, or the first payment ever used to that payee.',
            'problem'),
        (
            'Does anyone know how to stop this from happening and for it to automatically copy the description entered in the transaction narration?',
            'question')
    )
})
questions_sentences.append({
    'question_id': 138681,
    'sentences': (
        (
            'If you are a user of Xero and SmartTrade, tell us how you are getting on and your experience so far. Any tips?',
            'question'),
        (
            'About SmartTradeA comprehensive job management software system for trade & service businesses with a CRM module to build more information about your customers.',
            'context'),
        ('For more information, check out .',
         'context'),
        ('For general support, check out the  or this page for information on .',
         'context')
    )
})
questions_sentences.append({
    'question_id': 138861,
    'sentences': (
        (
            'I have a Stripe account and it is linked with Xero - when a client tries to pay via stripe they get an error message.',
            'problem'),
        ('I tried to pay a $1 account myself and got a message also.',
         'context'),
        ('Not sure why this is?',
         'question')
    )
})
questions_sentences.append({
    'question_id': 135489,
    'sentences': (
        ('Has anyone had success with setting up batch payments to vendors with Bank of America.',
         'question'),
        ('BOA does not appear to understand what I am trying to do.',
         'context'),
        ('I would like to use this feature to speed up our payment process.',
         'context')
    )
})
questions_sentences.append({
    'question_id': 137407,
    'sentences': (
        ('Hi all,New to Xero and seem to be having issues with importing pay run ABA files into our Westpac account.',
         'context'),
        ('I have checked that the correct BSB and Account number have been entered i.e. no spaces or hyphens.',
         'context'),
        (
            'I have also ticked the \"Include self-balancing transaction in the ABA file\" option and have included the \"DE User ID\" in the ABA file.',
            'context'),
        (
            'When I import the file into my Westpac account, I receive the following errors:Error -- An invalid Payment From account was used. Record Number 2 Invalid debit BSB format -- please check. Record Number 3 Record type must be 1The odd thing is that the BSB is correct and the record number does start with 1.',
            'problem'),
        (
            'Xero support recommended I contact the bank and after 2.5 hours of troubleshooting with Westpac, they said I need to go back to Xero...',
            'context'),
        ('Are there any other Xero/Westpac users that have successfully imported an ABA file for their pay run?',
         'question'),
        ('Cheers,Shaun',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 125697,
    'sentences': (
        ('I am setting up a new partnership.',
         'context'),
        ('There were several expenses prior to partnership opening their checking account.',
         'context'),
        ('How would I record these in xero?',
         'question'),
        ('I tried adding as expense receipt but then it wanted to reimburse me the bookkeeper.',
         'context')
    )
})
questions_sentences.append({
    'question_id': 136506,
    'sentences': (
        (
            'I was filing my sales taxes and noticed that the sales tax summary report produced different numbers than the the sales tax transactions report for the exact same period.',
            'problem'),
        ('Is there a reason why this would be happening.',
         'question'),
        ('After an hour of investigation, I can\'t seem to find the reason behind this.',
         'context'),
        (
            'I ended up using the sales tax transactions numbers for filing, as well as the total sales numbers pulled from the profit and loss report.',
            'context')
    )
})
questions_sentences.append({
    'question_id': 136890,
    'sentences': (
        ('Hello Can anyone help me please as I have a tricky problem?',
         'question'),
        (
            'The situation is staff are salaried (annual amount/hours = hourly rate) however they are paid monthly in arrears (last day of the month) for the actual number of days worked and not simply Annual salary / 12 months.',
            'context'),
        (
            'The issue is their leave needs to be calculated monthly Based on Ordinary Earnings for the month and not just 152 hours / 12 months.',
            'context'),
        ('When I try and put this into Xero AU Payroll it tells I have to insert a monthly amount of leave calculated.',
         'problem'),
        ('This is clearly different between months January and February as an example.',
         'context'),
        ('Any suggestions please?',
         'question'),
        ('Cab',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 135985,
    'sentences': (
        ('Hi,I sent this question into support a week ago, and still have not gotten a response.',
         'context'),
        ('I hope someone here can help me!',
         'context'),
        ('My accountant set up my bank feeds for me.',
         'context'),
        ('One of them is the situation where only the person who set up the feed can refresh it.',
         'context'),
        (
            'This bank feed fails all the time, and every time, like a pest, I have to email my accountant to refresh the feed for me.',
            'problem'),
        ('Both my accountant and I would prefer it if I could refresh the feed.',
         'context'),
        (
            'I understand that only the one who added the feed can refresh it - how can I be that person instead of my accountant?',
            'question'),
        ('If I am the only one who can refresh it, that is perfectly fine.',
         'context'),
        ('It\'s just a hassle when SHE is the only one who can refresh it.',
         'problem'),
        ('So is there any way to switch that over?',
         'question'),
        (
            'I\'ve tried looking around in Xero to figure out if I can re-enter the bank feed info so that then I will be the special *person* with the permissions, but I haven\'t been able to find any way to do that.',
            'context'),
        ('Suggestions?',
         'question'),
        ('Thanks so much,Heather',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 139566,
    'sentences': (
        ('I am looking for a SAS provider to compliment Xero.',
         'context'),
        ('Is anyone out there using such a service that they can recommend - I have heard of Huddle, Basecamp...',
         'question')
    )
})
questions_sentences.append({
    'question_id': 134965,
    'sentences': (
        (
            'We would love to find fellow Xero users in our supply chain and would even consider changing certain suppliers to Xero users for ease of use.',
            'context'),
        ('Trouble is there is not a subtle way of finding out who uses Xero.',
         'problem'),
        ('I thought there was a Xero user directory but can\'t find one.',
         'context')
    )
})
questions_sentences.append({
    'question_id': 133597,
    'sentences': (
        ('I have a client who operates his payroll for two shops.',
         'context'),
        (
            'It would be a good feature to be able to show the address of the location the employee works on the payslip rather than a single location for all.',
            'context')
    )
})
questions_sentences.append({
    'question_id': 135374,
    'sentences': (
        (
            'It\'s very common to invoice 50% of an invoice first and then on final invoice there\'s the next 50% and possibly additional expenses.',
            'context'),
        ('PLEASE XERO can you add this feature whereby I can deduct an amount already received/invoiced?',
         'question'),
        ('It would help a lot!',
         'context'),
        (
            'Instead I have to manually create another invoice to do this which completely defeats the purpose of having XERO in the first place.',
            'problem')
    )
})
questions_sentences.append({
    'question_id': 128780,
    'sentences': (
        ('Hi everyone.',
         'context'),
        ('I have been using Xero for my own small company for 2 years and its fantastic.',
         'context'),
        (
            'However one of my clients with 120 staff but an uncomplicated Architectural Business are concerned its too small for them.',
            'context'),
        ('Any thoughts, as I say its not a complicated business, no discounts, no inventory etc etc.',
         'question'),
        ('your thoughts would be appreciatedJoe',
         'outroduction')
    )
})
questions_sentences.append({
    'question_id': 140097,
    'sentences': (
        ('Who\'s the genius who thought the least important thing on a payslip was the payee\'s name?',
         'question'),
        ('Why on earth make that section in a smaller print than the majority of the document?',
         'question'),
    )
})

questions_sentences.append({
    'question_id': 125435,
    'sentences': (
        (
            'I have just completed my first financial year, and am confused about how to account for Corporation Tax in Xero.',
            'context'),
        ('I have submitted my tax return and just paid the tax due to HMRC.',
         'context'),
        (
            'I have reconciled the bank transaction so that now I have an Expense sitting against account 500 - Corporation Tax.',
            'context'),
        (
            'In my Profit and Loss for 2016-17, the expense against code 500 is now shown as an operating expense and reduces down the net profit for the year.',
            'problem'),
        (
            'Is there any way of separately showing net profit BEFORE tax (and having the Corporation Tax expense sitting between net profit BEFORE tax and net profit AFTER tax?).',
            'question'),
        ('Thanks,Ben',
         'outroduction')
    )
})

questions_sentences.append({
    'question_id': 137779,
    'sentences': (
        (
            'I have completed all of the payroll enrolment details in Payroll settings but Xero is not selecting any staff to be included in auto enrolment.',
            'problem'),
        ('All of them are eligible by my reckoning but none are selected.',
         'problem'),
        ('On the Employee tab under Eligibility Status the box is greyed out.',
         'problem'),
        (
            'I am clearly missing something but after assessing this forum and the videos I am no clearer what I am missing.',
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
        (
            "One thing that i would like to see is the credit invoices issued by suppliers to be able to be manually ticked against a payment rather than allocating it to another invoice.",
            'problem'),
        (
            'As a lot of our credit notes do not correspond with invoices from the supplier and it then becomes difficult for suppliers to match off our invoices from our remittances.',
            'problem'),
        (
            'Also the fact that each time you load an invoice onto a supplier that has a credit note, a reminder comes up that there is a credit note available,',
            'problem'),
        (
            "this in turn seems to stop the flow of creating another bill, as it takes you to that invoice if you dont allocate this credit.",
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
        (
            "Hi,I have reconciled also bank statement for past financial year from 1st April 2015 to 31st March 2016. I usually run monthly profit and loss reports.",
            'context'),
        (
            "However, for the final month of March the P&L report shows me as final conversion balances for the year ended March 2016 rather than the individual March month income and expenses.",
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
        (
            'One was because we were charged too much for shipping and the other because we were charged for an upgrade that we did not end up using.',
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
        (
            'If I just choose to reconcile it and label is as "vendor refund" is it categorized as an asset or as revenue?',
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
        (
            'I love the idea of being able to email an invoice to a customer with a big PAY NOW button, which will let them simply input their CC details secureley and pay their invoice.',
            'context'),
        (
            'This is a new venture for me, though, and I\'m admittedly ignorant on the details and variables I should be considering when making this.',
            'problem'),
        ("Which service should I integrate?",
         'question'),
        ('How do the services that integrate with Xero compare to setting up Merchant Services through my bank?',
         'question'),
        (
            'Would appreciate any guidance regarding how I might go about thinking about this problem and coming up with a good solution."),',
            'outroduction')
    )
})

questions_sentences.append({
    'question_id': 126082,
    'sentences': (
        ('Hi there,We use Capital On Tap as a regular loans service.',
         'context'),
        (
            "There is no option for bank feeds and the loan is paid in as and when we require it (almost like a transfer from a separate account with a loan limit).",
            'context'),
        (
            'We then have to pay back a minimum amount every month depending on the cumulative total we have loaned at the end of that month so the amount is never fixed, always variable.',
            'context'),
        (
            'I ideally want to record the capital we have received (ad hoc), the amount we have paid back (monthly) and the interest as an expense.',
            'context'),
        ("The loan was started before we began using Xero so I realise I will need to enter a conversion balance.",
         'context'),
        (
            'But I was wondering if anyone had any idea on how to go about recording the payments in, the repayments out and the interest.',
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
        (
            'I\'m just starting to reconcile after adding Kounta integration, and am not sure how to handle cash purchases made from the cash register.',
            'context'),
        (
            "If a supplier is paid cash on delivery from the till, the deducted cash is recorded as \"cash out\" showing the reduced cash in the till.",
            'context'),
        ('How do I record this invoice paid by cash in Xero?',
         'question'),
        (
            'The Kounta integration only shows the reduced cash in "cash register clearing account", not the COGS account.',
            'problem'),
        (
            "When you receive a purchase order in Kounta it doesn\'t appear to allow you to specify how the invoice was paid.",
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
        (
            "However I have a major problem today in that one of my clients is now registered for the Flat Rate Scheme at 12%.",
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
        (
            "We currently use CBUS clearing account however the CSV file they require every month is not downloadable from Xero.",
            'problem'),
        ('Does anyone else upload a file direct from Xero to a clearing house?',
         'question'),
        (
            'I tried to use the auto option in Xero through Click Super but as I need receipts to send to customers and neither Click or Xero can offer any reporting this is a dead end.',
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
        (
            "Ideally the POS system we would like touch screen based suitable for staff with limited computer skills or even iPad as we"
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
        (
            '"HiWe have some suppliers who have up to 70 invoices required for paymentTo avoid having to enter these all individually we create one purchase for the supplier,',
            'context'),
        (
            "and in the body of the purchase, enter all the invoices. Of course we are unable to list every invoice number in the reference box, so we call it by the month of statement.",
            'context'),
        (
            'It makes it very easy then to identity, pick up & batch all bills that need to be paid at the end of the month, as they all have the same reference.',
            'context'),
        (
            'This works fine for us, but we do get requests from our suppliers as to what invoices we are paying, as the remittance only says \'April 17 Statement\'.',
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
        (
            "but when I did there were invoices showing up as outstanding but when you drill into them it's been paid and the outstanding amount is $0",
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
        (
            "I followed the forum posts and set up the account code and put through as credit notes but I'm told this isn't what they want.",
            'problem'),
        (
            'Is it possible to put through a bad debt differently, such a journal entry, on an accrual scheme so that we can claim the VAT back but still'
            'leave the invoices open in case we do eventually get payments in?',
            'question'),
        (
            'We want to still be able to send statements etc, if requested, but adding a credit note to the invoices means that we are not able to do this as they\'re down as \'paid\',',
            'context')
    )
})
questions_sentences.append({
    'question_id': 128746,
    'sentences': (
        (
            '"Hi thereWe don\'t raise Xero invoices for our occasional suppliers, instead we\'ll simply create the transactions at reconciliation time,'
            'adding a new contact as necessary.',
            'context'),
        ("My question is -  what's the easiest way to search for these transactions by contact name?",
         'question'),
        (
            'I had a case this morning where I needed to quickly add a file to a historical transaction for a known contact and I had to do the following:- Start at the dashboard.'
            '- Click on Accounts -> Bank Accounts- Click the correct bank account.- Click the \'Transactions\' tab.- Click \'Search\', enter the contact name.'
            'Click the appropriate transaction from the list that appears.',
            'context'),
        ('That\'s quite laborious and also involves knowing which bank account the transaction belongs to.',
         'problem'),
        ("What am I missing here?",
         'question'),
        (
            'I tried, instead, to do it via the \'Contacts\' page, searched and found the correct contact, but there didn\'t seem to be a link to click through and view all'
            'transactions associated with that contact.',
            'problem'),
        (
            'Frustratingly, I could see a bar graph, visualising the transaction amounts, but no obvious way to view them.',
            'problem')
    )
})

questions_sentences.append({
    'question_id': 135892,
    'sentences': (
        ('Hi,This is a more general question about physical inventory management and not necessarily related to Xero'
         'but I figure that this is probably a good place to ask as I can\'t be the only person selling physical products',
         'context'),
        (
            "My business is wholesale alcohol business and we have to do regular inventory counts in our multiple warehouses.",
            'context'),
        ('At the moment this is done manually on paper and then transferred to excel.',
         'context'),
        (
            'I would like to move to a more automated system where the person doing the inventory count scans a product barcode and types in the number of items in the warehouse.',
            'context'),
        (
            "If this can be achieved with a barcode scanner that links wirelessly to an app on a tablet or phone it would be great.",
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

# DEVELOPER COMMUNITY DATA
questions_sentences.append({
    'question_id': 45917,
    'sentences': (
        ('Hi,The Australian Payroll API was recently updated to include USI (unique superannuation identifier).',
         'context'),
        (
            'I have an external system I connect to Xero that tries to match a super fund based on SPIN/USI, and I cannot search by USI via the API. ',
            'context'),
        (
            'When I to find a Super Fund via the API by querying on the new USI field, and it keeps returning an error "USI property is not supported for Where or Order clause".',
            'problem'),
        (
            'I can query by other fields e.g. SPIN Example query: /payroll.xro/1.0/SuperFunds?Where=USI%3D%3D%22TLS0100AU%22 ',
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
        (
            'I am getting reports from users of an error "Account could not be found" when sending their sales to Xero via the API.',
            'problem'),
        ('It appears that the accounts they are sending to exist, is there anything else that can cause this error?',
         'question')
    )
})

questions_sentences.append({
    'question_id': 46599,
    'sentences': (
        (
            'Hey!We are looking for a highly experianced developer who has is well versed in Ruby On Rails to intergrate veeqo.com with Xero.',
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
        (
            'when creating an invoice i include the contact record details (no guid) full details, this normally either creates a new contact or finds and existing one.',
            'context'),
        ('during testing i noticed that one of the contact matched even thou the company name was different.',
         'problem'),
        (
            'it then updated the contact and changed the company name.  Edited \t26 Jun 2014 3:20 p.m. \tSystem Generated \tName changed from \'OLD COMPANY\' to \'NEW COMPANY\'.',
            'context'),
        ('personally would have expected the new company to be created not some existing company updated.',
         'problem'),
        (
            'Can you please let me rules that are used for matching contacts as for some of the records i am processing i might have to create a contact in a separate call and pass in the guid instead.',
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
        (
            ' Example object object:SimpleXMLElement Object(    <Invoice> => SimpleXMLElement Object        (            <InvoiceID> => 4fa68953-c4cc-4c5e-ab64-5e9f38b6e0f5            <Type> => ACCREC            <Contact> => SimpleXMLElement Object                (                    <ContactID> => 85d15bf3-207f-4278-8449-e12dade98c66                )            <Date> => 2015-07-06            <DueDate> => 2015-07-06            <InvoiceNumber> => INV-0031            <CurrencyCode> => USD            <CurrencyRate> => 1.000000000000000            <Status> => AUTHORISED            <SentToContact> => false            <SubTotal> => 59.85            <TotalTax> => 5.24            <Total> => 65.09            <LineAmountTypes> => Exclusive            <UpdatedDateUTC> => 2015-07-06T13:10:46            <LineItems> => SimpleXMLElement Object                (                    <LineItem> => SimpleXMLElement Object                        (                            <AccountCode> => 200                            <TaxType> => TAX001                            <Description> => \'Fish out of Water: Finding Your Brand                            <Quantity> => 3.0000                            <UnitAmount> => 19.9500                            <ItemCode> => BOOK                            <TaxAmount> => 5.236875                            <LineAmount> => 59.85                            <DiscountRate> => 0.0000                        )                )        ))"),\'',
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
        (
            'One of them is that it does not contain our production data and the second one is that it expires after 30 days.',
            'problem'),
        (
            'The third problem is that it is bound to one account, which makes it harder for the developers to share one demo environment to test.',
            'problem'),
        ('Does Xero support a sandbox environment or an environment which is a copy of production?',
         'question'),
        (
            'Or is it possible to keep the demo environment alive for more then 30 days, including the sharing of the demo account?',
            'question'),
        ('Thanks and Regards,Keethanjan',
         'outroduction')
    )
})

questions_sentences.append({
    'question_id': 46320,
    'sentences': (
        (
            'I\'m wondering if there is any way to limit the number of results returned--for example, an equivalent to "SELECT TOP 100" in SQL.We intend to create about 800 invoices per month via the API, and all of them will be created on the same day and have the same invoice date and due date, so I don\'t think we could use any date fields or "if modified since" to limit the results.',
            'question'),
        (
            '  When issuing a GET request on these, ideally, we\'d be able to split it up into 8 different API calls; i.e.',
            'problem'),
        (
            'in the following pseudo code:\tRequest 1 of 8: Get the top 100 records where invoice date is 2012-04-02T00:00:00 order by UpdatedDateUTC\tRequest 2 of 8: Get the top 100 records where invoice date is 2012-04-02T00:00:00 and UpdatedDateUTC > (the last UpdatedDateUTC in Request 1) order by UpdatedDateUTC\tAnd so on, until there are no more records retrieved.\t',
            'code'),
        (
            'Is there any way either to limit the records returned or some other way to split up this request into multiple API calls?',
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
        (
            'The invoices passed from the two system will include the following details:1. Invoice Date 2. Invoice Number 3. Contact Name 4. Contact Address 5. Reference Number 6. Product Description 7. Product Quantity 8. Product Price 9. Currency 10. Delivery Cost 11. Sales Account 12. Tax Type',
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
        (
            'Even looking at the example implementations it is not a quick or easy thing to tease out the best way to implement and utilise this myself.',
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
        (
            'Hello, I\'ve got problem when trying to exchange request token to access token (sending request to /oauth/AccessToken).',
            'problem'),
        (
            'First step was completed successfuly and I redirected myself to /APIAuthorise.aspx page, where I authorized my app to access my account.',
            'context'),
        (
            'After redirecting me back to callback url I always get "oauth_problem=signature_invalid&oauth_problem_advice=Failed%20to%20validate%20signature" response from /oauth/AccessToken.',
            'problem'),
        (
            'Here are data I send and receive:This code is provided by the developer community - Xero does not warrant it in any wayI\'m pretty sure that signature is made correctly -',
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
        (
            'Hi,I am using the Xero API and sending a HTTP GET request from my application to Xero to return Contacts that match a certain Name.',
            'context'),
        (
            'So...using instructions from http://developer.xero.com/documentation/getting-started/http-requests-and-responses/#title3, I send (for example) Name="A Company Ltd" urlencoded as part of the URL.',
            'context'),
        ('This works fine, until I search on a Name that includes a double quote in it.',
         'problem'),
        ('Does anyone know how to get it to work and Xero to not return an error when a double quote exists?',
         'question'),
        (
            'I know it\'s highly unlikely that a Name would have a double quote in it, but it\'s always best to make an application as robust as possible in my opinion, no matter how unlikely.',
            'context'),
        ('Many thanks in advance.Cheers,Rhyd.',
         'outroduction')
    )
})

questions_sentences.append({
    'question_id': 45185,
    'sentences': (
        (
            'I\'m trying to return all Invoices for June 2013, NOT just those that have been changed since a certain date.',
            'context'),
        (
            'I can see how the API documentation handles this situation, it says to use the following value for the where parameter (from http://developer.xero.com/api-overview/http-requests-and-responses/#get-filtered):',
            'context'),
        ('FullyPaidOnDate >= DateTime(2011, 10, 01) AND FullyPaidOnDate <= DateTime(2011, 10, 30)',
         'code'),
        ('However I\'d like to use the useful xero.php wrapper if possible.',
         'problem'),
        (
            'After reading the github page and various discussions on here as well as the code, it looks to me as if the filter I should be setting is as follows (ie the \'value\' of the array item is itself an array made up of operand, literal value):',
            'context'),
        (
            '$aFilter = array(\t\'Date\' => array(\'>=\',\'DateTime(2013, 06, 01)\')\t,\'Date\' => array(\'<=\',\'DateTime(2013, 06, 30)\'));$result = $xero->Invoices(\'\',\'\',$aFilter,\'\');',
            'code'),
        (
            'However this results in the following error:Array(    [ErrorNumber] => 16    [Type] => QueryParseException    [Message] => Operator \'<=\' incompatible with operand types \'DateTime?\' and \'String\')',
            'problem'),
        (
            'Also of course as the field name is the array key, I only end up with one array item not two as you can see in the array dump:',
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
        (
            'We would like to ask what information you need from us so you can post details about COZYROC\'s solution here:https://developer.xero.com/code-samples/tools/overview/',
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
        (
            'With the latest revision of the app (no changes to the codeline used for the Timesheets upload), I am no longer able to do the uploads and am getting a BadRequest exception raised.',
            'problem'),
        ('The detail merely shows "A validation exception occurred".',
         'problem'),
        ('I have the Api.Timesheets.Create in a try/catch block, with three separate catch blocks.',
         'context'),
        (
            'The first of these is:catch (Xero.Api.Infrastructure.Exception.ValidationException vE){.....}but this is not trapping.',
            'problem'),
        ('The second catch block is for BadRequestException and that traps.',
         'context'),
        ('How can I then determine the actual Validation errors?',
         'question'),
        (
            'The full ValidationException block contains::\terrStore += "Validation errors from xero:\\r\\n";\tforeach (var v in vE.ValidationErrors)\t{\t\terrStore += v.Message + "\\r\\n";\t\tAppGlobals.logger.Error("Error: TS Upload error" + v.Message + "\\r\\n");\t}',
            'problem'),
        ('but with that not being trapped how can I find the errors?',
         'question'),
        (
            'Why does the BadRequest exception supersede the ValidationException, or are there multiple exceptions occurring?',
            'question'),
        (
            'It makes life fairly difficult when my client cannot determine what has gone wrong without my having to get into debug mode on a production system.',
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
        (
            'I want to test my application against different scenarios so it will be great if we can "induce" token expiration instead of having to wait 30 minutes for it to systematically expire.',
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
        (
            'Why is it that Xero will not accept an email address with numeric characters in the TLD either by API or manual Contact entry?',
            'question'),
        (
            'There are TLDs which have numeric character in them listed on IANA - http://data.iana.org/TLD/tlds-alpha-by-domain.txt  (scroll down to .XN domains).',
            'context'),
        (
            '(encoded as "xn--mgberp4a5d4ar") ("al-Saudiah") in Arabic Script,which is registered to the Saudi Network Information Centre',
            'context'),
        (
            'I get thrown this error via API:Error: 10 ValidationException A validation exception occurred Email address must be valid. Email address must be valid.',
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
        (
            'Have got it working using the core api Version 2 & have got hold of the payroll DotNet sample (which looks to be the same as the core api sample with a console payroll section).',
            'context'),
        (
            'Anyway the example doesn\'t show the situation where I wan to use both api\'s...i.e I want to process invoices using the core api and then turn the page to payroll and insert time-sheets.',
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
         'context'),
        ('I have an issue with the lineAmount when a CurrencyRate apply.',
         'problem'),
        (
            'This is one of my LineItems in my Invoice XML:LineItem\tDescription: EDGA01:INVBE3983:Travel\tLineAmount: 66.201300\tTaxAmount: 0.0000\tAccountCode: RET300\tCurrency fields as part of the Invoice XML:CurrencyCode: USDCurrencyRate: 0.0743The lineItem in the response from XERO, looked like this for the above line item:{          "Description": "EDGA01:INVBE3983:Travel",          "UnitAmount": 66.20,          "TaxType": "NONE",          "TaxAmount": 0.00,          "LineAmount": 66.20,          "AccountCode": "RET300",          "Tracking": ,          "Quantity": 1.0000,          "LineItemID": "732ca155-e1bc-4fe0-bb77-504f25540034",          "ValidationErrors": },',
            'code'),
        ('Why does the LineAmount change to 66.20, does XERO only accepts 2 decimal points?',
         'question'),
        ('Second scenario:I decided to send through the lineAmount with 2 decimal points.',
         'context'),
        (
            'This is one of my LineItems in my Invoice XML:LineItem\tDescription: ILLI11:INVBE3985:Setup\tLineAmount: 224.25\tTaxAmount: 0.00\tAccountCode: ASC400Currency fields as part of the Invoice XML:CurrencyCode: EURCurrencyRate: 0.0690',
            'code'),
        (
            'So according to my understanding Xero should do a reverse calculation for the value in the Revenue account: 224.25 % 0.0690 = R3250.00, but instead the Revenue account reports R3249.99',
            'problem')
    )
})

questions_sentences.append({
    'question_id': 45515,
    'sentences': (
        (
            'Hi,I am trying to modify a paid invoice by changing the account_code for given line item. I can modified unpaid invoice with out a problem.',
            'context'),
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
        (
            'We have different versions of same product running on cloud . each client has its own url like https ://<<clientname>>.ourproduct.com.',
            'context'),
        ('Will you please suggest what app type we should use ?',
         'question')
    )
})

questions_sentences.append({
    'question_id': 45329,
    'sentences': (
        (
            'Hi GuysI did a quick search for this but couldn\'t find an answer I was looking for. The documentation describes:  "Daily Limit: 5000 calls in a rolling 24 hour window"',
            'context'),
        (
            'We have different versions of same product running on cloud . each client has its own url like https ://<<clientname>>.ourproduct.com.',
            'context'),
        ('At what time does the count reset?',
         'question'),
        (
            'Is this relative to the API token you are using and when this is created, or is it every 00:00UTC? or at some other time?',
            'question'),
        (
            'I\'d like to track the API calls we make to ensure we throttle properly so we never hit the limit, however thats difficult to program unless I know when the API limits are reset.',
            'problem'),
        ('Thanks,Chris',
         'outroduction')
    )
})

questions_sentences.append({'question_id': 45018,
                            'sentences': (
                                (
                                    'Hi,I\'m using the .NET wrapper and want to use the Contact settings as default for the lineitem details.',
                                    'context'),
                                (
                                    'Specifically, I want to apply a discount or determine whether items are tax inclusive or exclusive based off of the account.',
                                    'problem'),
                                ('Can someone point out how to do that?',
                                 'question'),
                                (
                                    'Here\'s my code.Dim wInvoice As New XeroApi.Model.Invoice        Dim wContact As New XeroApi.Model.Contact        Dim Contact Name As String        ContactName = "Test Contact"        Dim myContacts = From contacts In repository.Contacts                         Where contacts.Name = ContactName        For Each myContact As XeroApi.Model.Contact In myContacts            Dim myContactID As String = myContact.ContactID.ToString            wContact.ContactID = New System.Guid(myContactID)            wInvoice.Contact = wContact            wInvoice.InvoiceNumber = "TEST"            wInvoice.Date = "10-29-2015"            wInvoice.Type = "ACCREC"            wInvoice.DueDate = "10-30-2015"            wInvoice.Status = "DRAFT"            wInvoice.LineItems = New XeroApi.Model.LineItems            Dim wLineItem = New XeroApi.Model.LineItem            wLineItem.Quantity = 2            wLineItem.Description = "Item1"            wLineItem.ItemCode = 9            wInvoice.LineItems.Add(wLineItem)            wLineItem = New XeroApi.Model.LineItem            wLineItem.Quantity = 3            wLineItem.Description = "Item2"            wLineItem.ItemCode = 1            wInvoice.LineItems.Add(wLineItem)            wLineItem = New XeroApi.Model.LineItem            wLineItem.Quantity = 4            wLineItem.Description = "Item3"            wLineItem.ItemCode = 17            wInvoice.LineItems.Add(wLineItem)            Dim sResults = repository.Create(Of XeroApi.Model.Invoice)(wInvoice)            If sResults.ValidationErrors.Count = 0 Then                MsgBox("Invoice Created")            Else                For Each something In sResults.ValidationErrors                    MsgBox(something.Message)                Next            End If        Next',
                                    'code'),
                                ('Thanks!',
                                 'outroduction'),

                            )
                            })

questions_sentences.append({
    'question_id': 45181,
    'sentences': (
        (
            'With a payment that is part of a bulk payment this returns the first purchase invoice associated with the bulk payment rather than the correct purchase invoice',
            'problem'),
        (
            'based on the payment amount it seems like a bulk payment divides into smaller payments but the invoice does not correspond)',
            'problem'),
        (
            'foreach (Payment vo_payment in repository.Payments.Where(x => (x.Date > datebegin && x.Date < dateend && !(x.Status == "DELETED" || x.Status == "VOIDED") && x.Invoice.Type == "ACCPAY")))                {                    vs_paymentstring = Convert.ToDateTime(vo_payment.Date).ToString("yyyyMMdd") + "_" + vo_payment.Invoice.InvoiceNumber + "_(" + vo_payment.PaymentID + ")";',
            'code')
    )
})

questions_sentences.append({
    'question_id': 45011,
    'sentences': (
        ('Hi there,Firstly, apologies if this is in the wrong place.',
         'context'),
        (
            'There were at least 3 possible places this question could\'ve been created, but I figured as I\'m using wrapper code it should go here.',
            'context'),
        ('I\'m using the .NET Xero API SDK 2.0.20 in C#.I\'m trying to send an invoice to a customer upon payment.',
         'context'),
        ('It should be sent with the invoice in a paid state (so there is no confusion).',
         'context'),
        ('I\'ve got the code down good to apply the payment to the invoice, and sending the e-mail goes fine.',
         'context'),
        (
            'But then when we try to update the invoice to say it\'s been sent out, I get the following validation errors:* "Invoice not of valid status for modification"* "This document cannot be edited as it has a payment or credit note allocated to it."',
            'problem'),
        (
            'Here is some of the code I\'m using. {\t// bits and bobs to get the payment made\t_privateAppApi.Payments.Create(payment);\tEmailInvoice(payment);\tUpdateXeroInvoiceSentToContact(payment.Invoice);}private void UpdateXeroInvoiceSentToContact(XeroModels.Invoice invoice){\tinvoice.SentToContact = true;\t_privateAppApi.Invoices.Update(invoice);}',
            'code'),
        ('Any ideas of how this could/should be handled?',
         'question'),
        (
            'I thought about trying to set the sent status first, then applying the payment and then sending the e-mail. The problem with this approach is that I\'d get caught out again if something went wrong sending the e-mail, I wouldn\'t then be able to set SentToContact to false, because a payment has been applied. Which doesn\'t feel quite right.',
            'problem'),
        ('Any help appreciated.Cheers,Craig',
         'outroduction')
    )
})

questions_sentences.append({
    'question_id': 45868,
    'sentences': (
        (
            'I am trying to work out the best way to update an existing Timesheet (Australian Payroll API), without replacing or overwriting the existing TimesheetLines.',
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
        (
            'I see that there is an ‘Allow access for 30 mins’ option, which saves them from having to login multiple times, however it still always prompts the user during this 30min period to select the Xero organisation.',
            'problem'),
        (
            'Is it possible for us to capture and store their Xero username / password, and the organisation that they have originally selected, within our software, so we can programmatically use them in the future?',
            'question'),
        (
            'So each time they would want to execute an import, they won’t have to login or select their organisation again. Is this possible to do with Xero?',
            'outroduction')
    )
})

questions_sentences.append({
    'question_id': 46210,
    'sentences': (
        ('Our AffinityLive product allows users to record expenses against a project.',
         'context'),
        (
            'In some cases they may not be personal expenses but ones paid for already by a business credit card or chequebook, etc.',
            'context'),
        ('We are wondering if these expenses can be pushed through to Xero via the API.',
         'question'),
        (
            'My understanding is that these are not Expense Claims assigned to a user, but are more general business expenses which are recorded differently.',
            'problem'),
        (
            'We\'re a bit lost on how to proceed - part of the problem of course is that we\'re not accountants and may be taking the wrong approach!',
            'problem'),
        ('Appreciate any advice.',
         'outroduction')
    )
})

update_db(questions_sentences)

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
