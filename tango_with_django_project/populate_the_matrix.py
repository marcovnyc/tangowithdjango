import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Category, Page


def populate():
    thematrix_cat = add_cat('thematrix',32,63)

    add_page(cat=thematrix_cat,
    title="The Matrix Theory",
    url="http://matrix.wikia.com/wiki/The_Matrix")

    add_page(cat=thematrix_cat,
    title="Neo, the One",
    url="http://matrix.wikia.com/wiki/Neo")

    add_page(cat=thematrix_cat,
    title="Agent Smith",
    url="http://matrix.wikia.com/wiki/Agent_Smith")

    themovies_cat = add_cat("The Movies",37,89)

    add_page(cat=themovies_cat,
    title="The Cast",
    url="http://matrix.wikia.com/wiki/Cast_of_The_Matrix")

    add_page(cat=themovies_cat,
    title="The Matrix trilogy",
    url="http://matrix.wikia.com/wiki/The_Matrix_(series)")

    add_page(cat=themovies_cat,
    title="10 Questions about the Matrix Trilogy",
    url="http://www.ifc.com/2015/06/10-questions-we-have-about-matrix-trilogy")

    history_cat = add_cat("The History of the Matrix",44,128)

    add_page(cat=history_cat,
    title="Bullet Time",
    url="https://www.youtube.com/watch?v=uPNBdDNZbYk")

    add_page(cat=history_cat,
    title="The Making of The Matrix",
    url="https://www.youtube.com/watch?v=uPNBdDNZbYk")

    # Print out what we have added to the other developers
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c

# Start exectuions here!
if __name__ == '__main__':
    print "Starting The Matrix Population script ..."
    populate()


