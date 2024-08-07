import { Component } from '@angular/core';
import { UserFormComponent } from './user-form/user-form.component';

@Component({
  selector: 'app-root',
  // standalone: false,
  template: '<app-user-form>Hello World</app-user-form>',
  // imports: [UserFormComponent]
})
export class AppComponent {}
