# mitrais_coding_test

### end point
- register page
{your_base_url}/mitrais/register
- login page
{your_base_url}/mitrais/view_login

- register API
{your_base_url}/mitrais/save_register

- login API
{your_base_url}/mitrais/register


### technology used

- Back-end Python Flask
all the end points are restfull APIs

then try them.
- Front-End
all page created with HTML, CSS BOOTSTRAP, JavaScript (Jquery included)

- APIs
APIs also provided, you can acces them with other apps frameworks

### Testing
- Manual unit test
take a look on mitrais_unit_test.pdf

- API testing
import the mitrais_test.postman_collection.json to postman collection 

### how to run

- install dependency
```bash
pip3 install -r requirement.txt
```
- import db
```bash
mysql -u root -p < mit_db.sql
```
- run program
```bash
python3 main.py
```
