import { Component, OnInit, Input } from '@angular/core';
import { SharedService } from 'src/app/shared.service';

@Component({
  selector: 'app-add-edit-dep',
  templateUrl: './add-edit-dep.component.html',
  styleUrls: ['./add-edit-dep.component.css']
})
export class AddEditDepComponent implements OnInit {

  constructor(private service:SharedService) { }

  //@Input() and @Output() give a child component a way to communicate with its parent
  /*
   1 Use the child's selector, here <app-item-detail>, as a directive within the parent component template.
   2 Use property binding to bind the item property in the child to the currentItem property of the parent.
   <app-item-detail [item]="currentItem"></app-item-detail>
   [item] is the target @Input()
  
  */
  @Input() dep:any;  // geting the values from my parent 
  //()'dep' === [dep]
  DepartmentId:string="";
  DepartmentName:string="";


  ngOnInit(): void {
    // when the add-edit-dep.component is activated we initialise the departmentId and departmentName with
    // the value from @Input() dep:any
    this.DepartmentId = this.dep.DepartmentId
    this.DepartmentName = this.dep.DepartmentName
  }

  addDepartment(){
    var val = {DepartmentId:this.DepartmentId,
              DepartmentName:this.DepartmentName}
    this.service.addDepartment(val).subscribe(res=>{
      alert(res.toString())
    })          
  }

  updateDepartment(){
    var val = {DepartmentId:this.DepartmentId,
              DepartmentName:this.DepartmentName}
    this.service.updateDepartment(val).subscribe(res=>{
      alert(res.toString())
    })          
  }

}
