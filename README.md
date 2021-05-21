# auctionsite
## Step 1:Login/Signup
### Packages:
- django-allauth
- django-crispy-forms

For user authentication i used django-allauth package to create signup and login page.
For better template view i also used django-crispy-forms in signup and login page.

## Step 2:Items list and detail view
### Packages:
- Pillow

To upload media files i used python image processing library Pillow which includes additional features such as basic validation.It is necessary to validate user upload files to ensure that it is not malicious.

I faced a problem to create item description page.The problem was to create a unique url using slug field as only primary key is not enough and sometimes it's vulnerable.The normal slug field cannot two items with same name.I solve this problem by defining a function which can generate random string for slug field. 

## Step 3:Auction Page

Here user can place bid items which are uploaded by others.After placing bid user can show his name in bid list and he can also edit his bid.

### Limitations:
- Bid can only be placed from admin panels.
- No logic is added whether the auction will end on auction end time or auction item will be gone from auction page.
