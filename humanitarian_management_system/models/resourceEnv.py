from humanitarian_management_system.models.resourceAllocator import ResourceAllocator
from humanitarian_management_system.models.resourceReport import ResourceReport
from humanitarian_management_system.models.resourceAdder import ResourceAdder
from humanitarian_management_system.models.resourceCampCreateDelete import ResourceCampCreateDelete
import pandas as pd
import pathlib as Path


r_inst = ResourceAllocator()

report_inst = ResourceReport()
table = report_inst.master_resource_stats()
print(table)