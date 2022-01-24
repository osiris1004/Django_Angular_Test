import { Injectable } from '@angular/core';

/*class HttpClient: Performs HTTP requests*/
import {HttpClient} from '@angular/common/http';

/*class Observable  provides support for delivering messages between different parts of your 
single-page application*/
// handle asychronous requests and responses
import {Observable} from 'rxjs';



@Injectable({
  providedIn: 'root'
})
export class SharedService {
  // add api url
readonly APIUrl = "http://127.0.0.1:8000";
// add photo url which we will be using to display photo profle
readonly PhotoUrl = "http://127.0.0.1:8000/media/";

//instantiate HttpClient in constructor
  constructor(private http:HttpClient) { }

  // NB the above function are execued in your ccc.component.ts when you want to do a request
  //to execute the it make: this.service.theFuntionCall

//  getDepList() : is a fucntion 
  getDepList():Observable<any[]>{
    //**his.http.get** : make a get request and <any[]> is the response type set to any. so it handle any type of propertie. 
    //**this.APIUrl+ 'nameOfUrl'** : set the url
    return this.http.get<any[]>(this.APIUrl + '/department/');
  }

  addDepartment(val:any){
    return this.http.post(this.APIUrl + '/department/',val);
  }

  updateDepartment(val:any){
    return this.http.put(this.APIUrl + '/department/',val);
  }

  deleteDepartment(val:any){
    return this.http.delete(this.APIUrl + '/department/'+val);
  }


  getEmpList():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl + '/employee/');
  }

 

  UploadPhoto(val:any){
    return this.http.post(this.APIUrl+'/SaveFile',val);

  }
}

