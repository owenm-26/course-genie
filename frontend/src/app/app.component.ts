import { Component } from '@angular/core';
import { UserFormComponent } from './user-form/user-form.component';

@Component({
  selector: 'app-root',
  // standalone: false,
  template: `
    @if (formSubmitted) {
      <h2>Thank you for submitting the form!</h2>
    }
    @else {
      <app-user-form (formSubmitted)="onFormSubmitted($event)" />
    }
    `,
  // imports: [UserFormComponent]
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  formSubmitted = false;

  onFormSubmitted(submitted: boolean) {
    this.formSubmitted = submitted;
    console.log(this.formSubmitted)
  }
}
