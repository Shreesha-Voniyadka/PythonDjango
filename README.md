### ================================= Project 1- Blog-Beginner ======================================

Django new infos:

1. CASCADE: When the referenced object is deleted, also delete the objects that have references to it (when you remove a blog post for instance, you might want to delete comments as well). SQL equivalent: CASCADE.

2. PROTECT: Forbid the deletion of the referenced object. To delete it you will have to delete all objects that reference it manually. SQL equivalent: RESTRICT.

3. RESTRICT: (introduced in Django 3.1) Similar behavior as PROTECT that matches SQL's RESTRICT more accurately. (See django documentation example)

4. SET_NULL: Set the reference to NULL (requires the field to be nullable). For instance, when you delete a User, you might want to keep the comments he posted on blog posts, but say it was posted by an anonymous (or deleted) user. SQL equivalent: SET NULL.

5. SET_DEFAULT: Set the default value. SQL equivalent: SET DEFAULT.

6. SET(...): Set a given value. This one is not part of the SQL standard and is entirely handled by Django.

7. DO_NOTHING: Probably a very bad idea since this would create integrity issues in your database (referencing an object that       actually doesn't exist). SQL equivalent: NO ACTION. (2)
