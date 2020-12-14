

<h1 align="center">
    Assignment Documentation
</h1>

<h5 align='justify'>Although django creates files automatically,but here some files are created to implemented the assignment. Below, discuss about the created files which were developed during implementation. In table-1, discuss about created files. Explanation is the overview of reason of created files.</h5>


| <h3 align="center">File Name</h3>|                                       <h3 align="center">Explanation</h3>                                                                           |
| :---                      |                                                                                                                                             ----: |
| <b>accounts/form.py</b>   | <p align="left">Created user interface which was mention in fieldbuzz ‘s documentation <b>section 4.1.1.1.</b></p>                                |
| <b>accounts/cookie.py</b> | <p align="left">Session-cookies based authentication created. The token is store in cookie during login time and it has expired time until the browser closed.</p>    |
| <b>accounts/utils.py</b>  | <p align="left">Implemented all the restriction that mentions in fieldbuzz’s documentation <b>section 3.2.1.5</b> and build up all the logical function.</p> |
| <b>accounts/decorators.py</b>| <p align="left">Controlling the permission using token which is based on session-cookies based authentication.</p>                              |

<p align="center">Table-1: Created Files List</p>

<div>
       <img align="right" src="https://user-images.githubusercontent.com/20153768/102019392-8e361180-3d9d-11eb-8ec3-86e1a47bbc81.png">
      <p align="left"><b>1.</b> After login (login), The API gives a token which is stored <b>[figure-1]</b> in cookies [<b>implemented in cookie.py]</b>.</p>
    
</div>
<p align="right" >Figure-1: store in cookies</p>


<p align='justify'><b>2.</b>The stored token is included as Authorization for both Recruitment Information API <b>[implemented in utils.py file]</b> and file upload API <b>[implemented in utils.py file]</b>. The token also used for permissions <b>[implemented in decorators.py]</b>.</p>
    <ul>
        <li>    Both <b>tysnic_id</b> generated <b>[implemented in utils.py]</b> based on email address. So, in this case email address act as a unique key.</li>
        <li>    <b>tysnic_id, email, cv’s tysnic_id and created time</b> are uploaded in database <b>[implemented in views.py]</b>. It would help to further update the information.</li>
        <li>    File restriction <b>[implemented in views.py, form.py]</b>; For example: pdf only, file’s size etc.</li>
    </ul>
    
<p><b>3.</b>  After posting data, both API return successful response <b>[implemented in view.py and result.html]</b>.  </p>
