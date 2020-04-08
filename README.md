# Consult


2x apps 'accounts' and 'fenlandlp'

accounts:

- extends user model with 1-1 'Profile' model
- related 'Organisation' model to stakeholders group by organisation and avoid duplicates and errors e.g. to avoid situations like: 'Environment Agency', 'EA', 'Env Agency' from arising
- related 'Client' model, so agents camn use same login to submit comments on behalf of there different clients (a small number of agents often represent many landowners)

-Following urls work (I think):

-/accounts/login
- /accounts/logout
- /signup - form with additional fields from Profile model, except 'Organisation' as this is a foreign key field (not sure what to do about this), and gdpr as this is a True/False field (just need to change field type)

- need to create a view to allow agents to add clients, add organisatiosn, and allow all users to edit their profile


fenlandlp:

- A basic blog app. The 'blog' represents the Local Plan, with 'posts' representing individual sections of the plan e.g. 'housing'

- Has following urls:

- /consult - plan index showing snippet of individual sections and sidebar to log in
- /consult/[post title] - section of plan showing comments, and comment form where logged in

- comment form grabs 'user' and 'post', and allows user to select their client from filtered list, type plain text and upload a supporting file
- comments must be approved in admin before they can be viewed


admin: 

- added all models, customised layout a bit
- Posts created using Summernote WYSIWYG editor, which looks pretty good but not as fancy as Wagtail. Only reason I'm not using Wagtail is I got a bit confused with views :-s
 
