from django.shortcuts import render, redirect

from poreikis.models import Dataset
from poreikis.forms import RequestForm


def index(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RequestForm()

    datasets = Dataset.objects.raw('''
        SELECT
            ds.id,
            ds.name,
            COUNT(DISTINCT req.project_id) AS projects
        FROM poreikis_dataset AS ds
        INNER JOIN poreikis_request_datasets AS rds ON (ds.id = rds.dataset_id)
        INNER JOIN poreikis_request AS req ON (rds.request_id = req.id AND req.project_id IS NOT NULL)
        GROUP BY
            ds.id,
            ds.name
        HAVING COUNT(DISTINCT req.project_id) > 0
    ''')

    return render(request, 'index.html', {
        'form': form,
        'datasets': datasets,
    })
