# To Run
- Clone the repo and cd into repo folder
- Install Requirements (pip install -r requirements.txt)
- Update SQLALCHEMY database config in app.py
- (Run Server) python app.py

# Approach
1) I chose to cleanly seperate the frontend from the backend favouring the use of API calls over templates
2) I created a very simple and straight forward API to create and list feature requests.
3) On the frontend, I adopt a simple layout favoring the concept of a one page application where a user is able to access all app functionalities without having to browse to different pages.
4) The only functionalities provided are create feature request and list feature requests. I chose these 2 as they are fundamental to providing business value to customers that request for features

## Improvements

1) Additional functionalities such as being able to update or delete feature requests can easily be added/implemented

2) It can be argued for or against that business rules need to be applied to determine whether or not a client should be able to change/update their feature request.

3) And also whether feature requests once created, can be deleted.

4) As such, a configuration system would be needed where we can configure such rules on a per client basis.

