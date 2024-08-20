import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CourseResultsComponent } from './course-results.component';

describe('CourseResultsComponent', () => {
  let component: CourseResultsComponent;
  let fixture: ComponentFixture<CourseResultsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [CourseResultsComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CourseResultsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
