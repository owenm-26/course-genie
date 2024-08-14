import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

// specifies data types for form data
interface FormData {
  name: string;
  email: string;
  term: string;
  numCredits: string;
  desiredHubs: string;
}

@Injectable({
  providedIn: 'root'
})
export class FormService {

  // TODO: for the apiUrl it would be best practice to get at least the port from the env file probably?

  private apiUrl = 'http://localhost:8000/api/form'; // original file submission api call
  private apiSolveBaseUrl = 'http://localhost:8000/api/setupsolve'; // api url to set up backend infrastructure and solve

  constructor(private http: HttpClient) { }

  submitForm(data: any): Observable<any> {
    const apiSolveUrl = `${this.apiSolveBaseUrl}/${data.numCredits}/${data.desiredHubs}`;
    return this.http.get(apiSolveUrl);
    // return this.http.post(this.apiUrl, data)
  }
}
