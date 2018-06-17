__author__ = 'me'

BEGIN = """
<!DOCTYPE html>
<html>
<head>
<style>
table, th, td {
    border: 0.5px solid green;
}
</style>
</head>
<body>

<table>
"""
CAPAT_TABEL = """
  <tr>
    <th><center>{:s}</center></th>
    <th><center>{:s}</center></th>
  </tr>
"""

INTRARE_TABEL = """
  <tr>
    <td><center>{:s}</center></td>
    <td><center>{:s}</center></td>
  </tr>
"""

END = """
</table>

</body>
</html
"""


f = open("table.html", 'w')
f.write(BEGIN)
f.write(CAPAT_TABEL.format("nume", "activitate"))
f.write(INTRARE_TABEL.format("asdsadsadsa, "asdsadsadsa"))



f.close()
