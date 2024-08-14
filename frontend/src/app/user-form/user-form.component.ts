import { Component, EventEmitter, Output } from '@angular/core';
import { FormService } from '../form.service';

@Component({
  selector: 'app-user-form',
  template: `
    <div class="form-container">
      <form (ngSubmit)="onSubmit()">
        <div class="form-group">
          <label for="name">Name:</label>
          <input type="text" id="name" [(ngModel)]="formData.name" name="name" required>
        </div>

        <div class="form-group">
          <label for="email">Email:</label>
          <input type="email" id="email" [(ngModel)]="formData.email" name="email" required>
        </div>

        <div class="form-group">
          <label for="term">Term:</label>
          <select [(ngModel)]="formData.term" name="term">
            <option value="Fall 2024">Fall 2024</option>
          </select>
        </div>

        <div class="form-group">
          <label for="numCredits">Number of HUB credits desired:</label>
          <select [(ngModel)]="formData.numCredits" name="numCredits">
            @for(val of creditOptions; track val) {
              <option value={{val}}>{{ val }}</option>
            }
          </select>
        </div>

        <div class="form-group">
          <label for="desiredHubs">Choose the HUBs you need:</label>
          <select multiple [(ngModel)]="formData.desiredHubs" name="desiredHubs">
            @for(hub of hubOptions; track hub[0]) {
              <option value={{hub[1]}}>{{ hub[0] }}</option>
            }
          </select>
        </div>

        <button type="submit" class="submit-button">Submit</button>
      </form>
    </div>
  `,
  styleUrls: ['./user-form.component.css']
})
export class UserFormComponent {
  @Output() formSubmitted = new EventEmitter<boolean>();  // New EventEmitter to notify form submission

  formData = { 
    name: '', 
    email: '', 
    term: 'Fall 2024', 
    numCredits: '16', 
    desiredHubs: ''
  };
  creditOptions: number[] = [4, 8, 12, 16, 20];
  hubOptions: [string, string][] = [
    ["Historical Context", "historical_context"],
    ["Individual In Community", "individual_in_community"],
    ["Research And Information", "research_and_information"],
    ["Social Inquiry 2", "social_inquiry_2"],
    ["Global Citizenship", "global_citizenship"],
    ["Writing Intensive", "writing_intensive"],
    ["Ethical Reasoning", "ethical_reasoning"],
    ["Critical Thinking", "critical_thinking"],
    ["Creativity And Innovation", "creativity_and_innovation"],
    ["Teamwork And Collaboration", "teamwork_and_collaboration"],
    ["Scientific Inquiry 1", "scientific_inquiry_1"],
    ["Digital Multimedia", "digital_multimedia"],
    ["Oral And Signed Communication", "oral_and_signed_communication"],
    ["Aesthetic Exploration", "aesthetic_exploration"],
    ["Philosophical Inquiry", "philosophical_inquiry"],
    ["First Year Writing", "first_year_writing"]
  ]

  // I think this may be a more complete set of hub options
  // hubOptions: string[] = ['Aesthetic Exploration', 'Creativity/Innovation', 'Critical Thinking', 'Digitial/Multimedia', 
  // 'Ethical Reasoning', 'First-Year Writing Seminar', 'Global Citizenship', 'Historical Consciousness', 'Oral/Signed Communication',
  // 'Philosophical Inquiry', 'Quantitative Reasoning I', 'Quantitative Reasoning II', 'Research and Information', 'Scientific Inquiry I',
  // 'Scientific Inquiry II', 'Teamwork/Collaboration', 'Writing, Research, Inquiry', 'Writing-Intensive Course'];

  // converts form response hubs to binary hub string
  convertHubsToString() {
    let hubString = ""
    let desiredHubsIndex = 0
    for(let i = 0; i < this.hubOptions.length; i++) {
      if (this.hubOptions[i][1] == this.formData.desiredHubs[desiredHubsIndex]) {
        hubString += '1';
        desiredHubsIndex += 1;
      } else {
        hubString += '0';
      }
      this.formData.desiredHubs = hubString
    }
  }

  // TODO: converts get request response binary hub string to hubs
  // convertStringToHubs(string) {
  //   let res: string[] = []
  //   for(let i = 0; i < this.hubOptions.length; i++) {
  //     if (this.hubOptions[i] == ) {
  //       hubString += '1';
  //       desiredHubsIndex += 1;
  //     } else {
  //       hubString += '0';
  //     }
  //     this.formData.desiredHubs = hubString
  //   }
  // }

  constructor(private formService: FormService) {}

  onSubmit() {
    this.convertHubsToString()
    this.formService.submitForm(this.formData)
      .subscribe(response => {
        console.log('Server response:', response); // probably figure out how to send that data to decode that and then send it to the frontend where it thanks you for submitting
        this.formSubmitted.emit(true);  // Emit the event when the form is submitted
      }, error => {
        console.error('Error:', error);
      });
  }
}

