import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ProjetsService {

  constructor(private httpClient: HttpClient){}
    getData(){
      return this.httpClient.get('https://api.bie-innov.com/v1/projets')
    }}