import unittest
from app.models import Blog, Comments, User

class UserTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(password = 'kkkkk')

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('kkkkk'))



class TestComments(unittest.TestCase):
    def setUp(self):
        self.comments = Comments(comment='We are safe')
    
    def tearDown(self):
        Comments.query.delete()

    def test_save_comment(self):
        self.new_comment.save_comments()
        self.assertTrue(len(Comments.query.all())>0)




