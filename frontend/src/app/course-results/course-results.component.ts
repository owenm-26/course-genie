import { Component, Input, OnInit } from '@angular/core';
import { FormService } from '../form.service';

@Component({
  selector: 'app-course-results',
  template: `
  <div *ngIf="courseDetails.length > 0">
    <h2>Course Details</h2>
    <div *ngFor="let course of courseDetails">
      <h3>{{ course.course_name }}</h3>
      <p>{{ course.class_room }}</p>
      <p>{{ course.start_time }} </p>
      <p> {{ course.schedule_id }} </p>
      <p> {{ course.schedule }} </p>
    </div>
  </div>

  <div *ngIf="courseDetails.length === 0">
    <p>No course details available.</p>
  </div>
  `,
  styleUrls: ['./course-results.component.css']
})
export class CourseResultsComponent implements OnInit {
  @Input() courseIds: string[] = [];  // The course IDs received from the parent component
  courseDetails: any[] = []; // Array to hold the details of the courses

  constructor(private formService: FormService) {}

  ngOnInit(): void {
    this.loadCourseDetails();
  }

  loadCourseDetails() {
    if (this.courseIds.length > 0) {
      this.formService.getCourseDetails(this.courseIds)
        .subscribe(response => {
          this.courseDetails = response.data;  // Assuming response.data holds the course details
        }, error => {
          console.error('Error fetching course details:', error);
        });
    }
  }
}
