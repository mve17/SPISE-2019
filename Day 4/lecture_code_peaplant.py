import random

class PeaPlant():
	def __init__(self, flower_allele_1, flower_allele_2, stem_allele_1, 
	             stem_allele_2):
		self.flower_genotype = (flower_allele_1, flower_allele_2)
		self.stem_genotype = (stem_allele_1, stem_allele_2)
	def get_genotype(self):
		return (self.flower_genotype, self.stem_genotype)
	def get_phenotype(self):
		if self.flower_genotype == ('white', 'white'):
			flower_phenotype = 'white'
		else:
			flower_phenotype = 'purple'
		if self.stem_genotype == ('short', 'short'):
			stem_phenotype = 'short'
		else:
			stem_phenotype = 'long'
		return (flower_phenotype, stem_phenotype)
	def __add__(self, other_plant): # Breeding operation
		# Randomly chooses an element of the flower_genotype attribute
		flower_allele_1 = random.choice(self.flower_genotype) 
		flower_allele_2 = random.choice(other_plant.flower_genotype)
		stem_allele_1 = random.choice(self.stem_genotype)
		stem_allele_2 = random.choice(other_plant.stem_genotype)
		return PeaPlant(flower_allele_1, flower_allele_2, stem_allele_1, 
		                stem_allele_2)
	
def build_random_pea_plant():
	flower_alleles = ['white', 'purple']
	stem_alleles = ['short', 'long']
	return PeaPlant(random.choice(flower_alleles), 
	                random.choice(flower_alleles), 
	                random.choice(stem_alleles), 
	                random.choice(stem_alleles))


