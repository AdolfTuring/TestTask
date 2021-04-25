# TestTask
http://127.0.0.1:8000/ - list of folowing users posts. Method POST accept:{"id":23,"action":"read"} or {"id":23,"action":"unread"} argument for add tag read. n/
http://127.0.0.1:8000/<int:pk>- single post object. n/
http://127.0.0.1:8000/create/ - page for making posts. Accept {"title":"Some title","text":"some text"} argument for making posts, author are authenthificated user. n/
http://127.0.0.1:8000/users/ - list of users read only. n/
http://127.0.0.1:8000/users/<str:name> - User blog. Method POST accept {"action":"follow"} or {"action":"unfollow"} for folowing specific user.. n/
Method GET show all users post orderd bu publicated date.. n/

login:Admin password: qwerty. n/
login:User1 password: zxcvbn123zxc. n/
login:User2 password: zxcvbn123zxc. n/

add new user via admin page.. n/
