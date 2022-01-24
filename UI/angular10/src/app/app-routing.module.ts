import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

// import the component here in which we will perform the rpute
import {EmployeeComponent} from './employee/employee.component';
import {DepartmentComponent} from './department/department.component';

// the route array is where whe add the route 
const routes: Routes = [
  //{path: 'url', component:displayComponent } = if i type url, the displayComponent will be shown
  {path:'employee',component:EmployeeComponent},
  {path:'department',component:DepartmentComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
