from django.contrib.postgres.fields import ArrayField
from django.db import models

from backend.fpseq.util import slugify
from ..util.helpers import shortuuid

class Repeat(models.Model):
    id = models.CharField(primary_key=True, max_length=22, default=shortuuid, editable=False)
    name = models.CharField(max_length=200, blank=True, null=True, unique=True)
    slug = models.SlugField(max_length=200, blank=True, null=True)
    aliases = ArrayField(
        models.TextField(blank=True, null=True),
        blank=True,
        null = True
    )
    motif = models.TextField(blank=True, null=True)
    proteomics = models.TextField(blank=True, null=True)
    parental_organism = models.ForeignKey(
        "Organism",
        # related_name="organism",
        verbose_name="Parental organism",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Organism from which the protein was engineered",
    )
    # references = models.ForeignKey(
    #     "Reference",
    #     related_name="reference",
    #     verbose_name="Reference",
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     null=True,
    #     help_text="References for repeats",
    # ),
    references = models.TextField(blank=True, null=True)

    def aliases_as_str(self):
        if not self.aliases:
            return ""
        return ", ".join(self.aliases)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
    def get_proteins(self):
        return self.proteintf_set.all()
