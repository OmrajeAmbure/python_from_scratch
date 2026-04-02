"""
NamedTuple :-
A NamedTuple is like a regular tuple but with named fields, making data more readable and accessible. Instead of using indexes, you can access elements by name (e.g., student.fname), which improves code clarity and ease of use.
Syntax:
class collections.namedtuple(typename, field_names)
"""
from collections import namedtuple

student = namedtuple('student',['name','age','DOB']);
s = student("omraje",21,'27/05/2005');

print(s[1]); # 21
print(s.DOB)


"""
Conversion Operations  -->
1. _make(): This function is used to return a namedtuple() from the iterable passed as argument.
2. _asdict(): This function returns the OrdereDict() as constructed from the mapped values of namedtuple().
"""
from  collections import namedtuple

student = namedtuple('student',['name','age','DOB']);
s = student("omraje",21,'27/05/2005');
li = ['manjoot','19','411997']
di = {'name':'omraje','age':21,'DOB':'1391997'};

print(student._make(li)); # tudent(name='manjoot', age='19', DOB='411997')
print(s._asdict()); # {'name': 'omraje', 'age': 21, 'DOB': '27/05/2005'}

