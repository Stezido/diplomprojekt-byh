package KisModel;

import FhirModel.Organization;

import java.util.Set;

public class MedicaldepartmentWrapper {

    public Set<MedicalDepartmentK> getData() {
        return data;
    }

    public void setData(Set<MedicalDepartmentK> data) {
        this.data = data;
    }

    Set<MedicalDepartmentK> data;
}
