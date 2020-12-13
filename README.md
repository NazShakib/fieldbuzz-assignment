<h1 align="center">
    Assignment Documentation
</h1>

<h5 align='justify'>There have some created and updated files to implemented the assignment. Below, discuss about the created and updated files which were developed during implementation. In table-1, discuss about created files. Explanation is the overview of reason of created files.</h5>


| File Name                 |                                       <p align="center">Explanation</p>                                                                           |
| :---                      |                                                                                                                                             ----: |
| accounts/form.py          | Created user interface which was mention in fieldbuzz ‘s documentation section 4.1.1.1.                                                           |
| accounts/cookie.py        | Session-cookies based authentication created. The token is store in cookie during login time and it has expired time until the browser closed.    |
| accounts/utils.py         | Implemented all the restriction that mentions in fieldbuzz’s documentation section 3.2.1.5 and build up all the logical function.                 |
| accounts/decorators.py    | Controlling the permission using token which is based on session-cookies based authentication.                                                    |
