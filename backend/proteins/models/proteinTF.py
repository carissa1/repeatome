from django.contrib.postgres.fields import ArrayField
from django.db import models

from ..util.helpers import shortuuid
from references.models import Reference

class ProteinTF(models.Model):
    id = models.CharField(primary_key=True, max_length=22, default=shortuuid, editable=False)
    gene = models.SlugField(max_length=200, blank=True, null=True, unique=True)
    aliases = ArrayField(
        models.TextField(blank=True, null=True),
        blank=True,
        null=True
    )
    gene_type = ArrayField(
        models.TextField(blank=True, null=True),
        blank=True,
        null = True
    )
    gene_family = models.TextField(blank=True, null=True)
    dna_binding_domain = models.TextField(blank=True, null=True)
    signaling_pathway = models.TextField(blank=True, null=True)
    satellite = models.TextField(blank=True, null=True)
    validation_grade = models.TextField(blank=True, null=True)
    prediction_method = models.TextField(blank=True, null=True)
    microscopy_result = models.JSONField(default=dict, blank=True, null=True)
    motif_enrichment = models.DecimalField(decimal_places=5, max_digits=10, blank=True, null=True)
    motif_q_score = models.DecimalField(decimal_places=5, max_digits=10, blank=True, null=True)
    existing_images = models.TextField(blank=True, null=True)
    existing_images_link = models.TextField(blank=True, null=True)
    existing_fusion = models.TextField(blank=True, null=True)
    cloned_fusion = models.TextField(blank=True, null=True)
    imaging_results = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    ENSEMBL = models.TextField(blank=True, null=True)
    UNIPROT = models.TextField(blank=True, null=True)
    PDB = models.TextField(blank=True, null=True)
    micro_url = models.TextField(blank=True, null=True)
    AF3 = models.TextField(blank=True, null=True)
    proteomics_url = models.TextField(blank=True, null=True)
    rna_url = models.TextField(blank=True, null=True)
    jaspar =  models.TextField(blank=True, null=True)
    # slug = models.SlugField(max_length=200, blank=True, null=True) # for link to specific protein
    protein_sequence = models.TextField(blank=True, null=True)
    articles = models.ForeignKey(
        Reference,
        related_name="articles",
        verbose_name="reference",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="References for protein",
        to_field='doi'
    )
