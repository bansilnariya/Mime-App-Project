from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

data="""

<table>
    <tr>
        <th>eid</th>
        <th>ename</th>
        <th>esal</th>
    </tr>
    <tr>
        <td>10001</td>
        <td>Bansil</td>
        <td>2000</td>
    </tr>
    <tr>
        <td>10002</td>
        <td>Meet</td>
        <td>4000</td>
    </tr>
    <tr>
        <td>10003</td>
        <td>Pratik</td>
        <td>6000</td>
    </tr>
</table>"""

class htmlview(View):
    def get(self,request):
        return HttpResponse(data,content_type="text/html")

class excelview(View):
    def get(self,request):
        return HttpResponse(data,content_type="vnd.ms-excel")
class xmlview(View):
    def get(self,request):
        return HttpResponse(data,content_type="apllicatin/xml")