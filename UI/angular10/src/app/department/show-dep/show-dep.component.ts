import { Component, OnInit } from '@angular/core';
import { SharedService } from 'src/app/shared.service';

@Component({
  selector: 'app-show-dep',
  templateUrl: './show-dep.component.html',
  styleUrls: ['./show-dep.component.css']
})
export class ShowDepComponent implements OnInit {

  // instantiate SharedService in constructor
  constructor(private service:SharedService) { }

  // the below following are variable created
  DepartmentList:any=[];
  ModalTitle:string="";
  ActivateAddEditDepComp:boolean=false;
  dep:any;
  DepartmentIdFilter:string="";
  DepartmentNameFilter:string="";
  DepartmentListWithoutFilter:any=[];

  //ngOnInit is the first methode that get executed when this componet is in scope
  ngOnInit(): void {
    this.refreshDepList();
  }

  
  addClick(){
    // function that submit value after a click
    this.dep = {
      DepartmentId:0,
      DepartmentName:"",
    }
    this.ModalTitle = "add books";
    this.ActivateAddEditDepComp = true;
  }

  closeClick(){
    //deactivate the component 
    this.ActivateAddEditDepComp=false;
    //refrech the data after an add or edit has been made
    this.refreshDepList();
   
  }

  editClick(item:any){
    //send the details to dep
    this.dep = item;
    this.ModalTitle ="Edit book";
    this.ActivateAddEditDepComp = true
  }

  deletClick(item:any){
    this.service.deleteDepartment(item.DepartmentId).subscribe(res=>{
      alert(res.toString())
      this.refreshDepList();
    })          
  }

// methode for refreching our data
  refreshDepList(){
    //Publishers are the one who publishes the data and Subscribers are the ones who consume the data.  
    //Observables will be connected to observers and whenever they observe a new value or change in data, they will execute code with the help of Subscription and all the subscribed components will receive the updated outcome.  
    //subcriber make sure to wait untill a response is recieved from API call, and then assigne the value data
    this.service.getDepList().subscribe(data=>{
      this.DepartmentList=data;
    });
  }

}