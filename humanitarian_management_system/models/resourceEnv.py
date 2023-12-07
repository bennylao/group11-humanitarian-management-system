from humanitarian_management_system.models.resourceAllocator import ResourceAllocator
from humanitarian_management_system.models.resourceAdder import ResourceAdder
from humanitarian_management_system.models.resourceReport import ResourceReport
from humanitarian_management_system.models.resourceCampCreateDelete import ResourceCampCreateDelete

from pathlib import Path
import pandas as pd

instance = ResourceCampCreateDelete()
report_instance = ResourceReport()

alloc_instance = ResourceAllocator()

alloc_instance.manual_alloc()