We are given a Group class and some initial data to test agains our solution, we are asked to write a `is_user_in_group` that needs to check if an user is in a group of in children groups/users ...

As we have to go over a Group hierarchy I decided to use a recursive solution, so begining on the first group we check if an user exists there and if not but there are subgroups in that group we use the recursive approach to go over the children groups.

## Time complexity

It depends on the number of iterations that are launched. It will depend on the **groups (g)** and he **number of users (u)** of a folder, being the time complexity of **O(g\*u)**
Being in this case dependent on **encapsulation of groups** and **number of users** of folders, resulting in a **O(g\*u)**.

## Space complexity

It is dependent on the number of returns the function does, in this case **O(1)**.
