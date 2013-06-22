# -*- coding: utf-8 -*-
from django.db import models


class Transaction(models.Model):
    TYPES = (
        ('Income', 'Έσοδα'),
        ('Expenses', 'Έξοδα'),
    )
    CATEGORIES = (
        ('Sindromi', 'Συνδρομή'),
        ('Dorea', 'Δωρεά'),
        ('Enoikio', 'Ενοίκιο'),
        ('Reuma', 'Ρεύμα'),
        ('Exoplismos', 'Εξοπλισμός'),
        ('Propaganda', 'Προπαγάνδα'),
        ('Promithies', 'Προμήθειες'),
        ('Internet', 'Internet'),
        ('Nero', 'Νερό'),
        ('Trapeza', 'Τράπεζα'),
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    typeof = models.CharField(max_length=8, choices=TYPES, default="Income")
    created = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=10, choices=CATEGORIES,
                           default="Sindromi")
    source = models.CharField(max_length=40)
    comment = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ["-created"]
