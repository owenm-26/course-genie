import { Component } from '@angular/core';
import { UserFormComponent } from './user-form/user-form.component';
import { CourseResultsComponent } from './course-results/course-results.component';

@Component({
  selector: 'app-root',
  // standalone: false,
  template: `
    @if (formSubmitted) {
      <h2>Thank you for submitting the form!</h2>
      <div class="results-container">
        <app-course-results [courseIds]="selectedCourseIds"></app-course-results>
      </div>
    }
    @else {
      <app-user-form (formSubmitted)="onFormSubmitted($event)"/>
    }
    `,
  // imports: [UserFormComponent]
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  formSubmitted = false;
  selectedCourseIds: string[] = [];  // Holds the course IDs after form submission (TODO: pass data back from user-form.component)

  onFormSubmitted(event:{ submitted: boolean, selectedCourseIds: number[]}) {
    this.formSubmitted = event.submitted;
    this.selectedCourseIds = event.selectedCourseIds.map(String)
    console.log(this.formSubmitted)
    console.log(this.selectedCourseIds)
  }
}
