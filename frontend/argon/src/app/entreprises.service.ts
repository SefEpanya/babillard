import { Injectable} from '@angular/core';
import { HttpClient } from '@angular/common/http';
// import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class EntreprisesService{

  constructor(private httpClient: HttpClient){}
    getData(){
      return this.httpClient.get('https://api.bie-innov.com/v1/')
    }
  }
