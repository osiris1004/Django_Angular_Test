import { Component } from '@angular/core';

@Component({
  /*
    A selector is use to insert an instance of this component wherever it finds the 
    corresponding tag in template HTML.
  */
  selector: 'app-root',
  /*
      The relative path or absolute URL of a template file for an Angular component
  */
  templateUrl: './app.component.html',

  /* 
      One or more relative paths or absolute URLs for files containing CSS stylesheets 
      to use in this component.
  */
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'angular10';
}
 