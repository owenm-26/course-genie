// import { Component } from '@angular/core';
// import { HttpClient } from '@angular/common/http';
// import { FormsModule } from '@angular/forms';
// import { CommonModule } from '@angular/common';

// @Component({
//   selector: 'app-user-form',
//   standalone: false,
//   // imports: [CommonModule, FormsModule],
//   templateUrl: './user-form.component.html',
//   // template: `
//     // <form (ngSubmit)="onSubmit()">
//     //   <label for="name">Name:</label>
//     //   <input type="text" id="name" [(ngModel)]="formData.name" name="name" required>

//     //   <label for="email">Email:</label>
//     //   <input type="email" id="email" [(ngModel)]="formData.email" name="email" required>

//     //   <button type="submit">Submit</button>
//     // </form>
//   // `
// })
// export class UserFormComponent {
//   formData = { name: '', email: '' };

//   constructor(private http: HttpClient) {}

//   onSubmit() {
//     this.http.post('/api/form', this.formData)
//       .subscribe(response => {
//         console.log('Server response:', response);
//       }, error => {
//         console.error('Error:', error);
//       });
//   }
// }

import { Component } from '@angular/core';
import { FormService } from '../form.service';

@Component({
  selector: 'app-user-form',
  templateUrl: './user-form.component.html',
  styleUrls: ['./user-form.component.css']
})
export class UserFormComponent {
  formData = { name: '', email: '' };

  constructor(private formService: FormService) {}

  onSubmit() {
    this.formService.submitForm(this.formData)
      .subscribe(response => {
        console.log('Server response:', response);
      }, error => {
        console.error('Error:', error);
      });
  }
}

